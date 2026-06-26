const form = document.getElementById("generate-form");
const promptInput = document.getElementById("prompt");
const modeSelect = document.getElementById("mode");
const submitBtn = document.getElementById("submit-btn");

const progressSection = document.getElementById("progress-section");
const progressFill = document.getElementById("progress-fill");
const progressMessage = document.getElementById("progress-message");

const resultSection = document.getElementById("result-section");
const resultContent = document.getElementById("result-content");

const errorSection = document.getElementById("error-section");
const errorMessage = document.getElementById("error-message");

const newRequestBtn = document.getElementById("new-request-btn");
const retryBtn = document.getElementById("retry-btn");

let pollTimer = null;

function hideAllSections() {
    progressSection.classList.add("hidden");
    resultSection.classList.add("hidden");
    errorSection.classList.add("hidden");
}

function showProgress(progress, message) {
    hideAllSections();
    progressSection.classList.remove("hidden");
    progressFill.style.width = `${progress}%`;
    progressMessage.textContent = message;
}

function showError(message) {
    hideAllSections();
    errorSection.classList.remove("hidden");
    errorMessage.textContent = message;
    submitBtn.disabled = false;
}

function showResult(result) {
    hideAllSections();
    resultSection.classList.remove("hidden");
    submitBtn.disabled = false;

    if (result.mode === "chat") {
        resultContent.innerHTML = `
            <p><strong>Провайдер:</strong> ${escapeHtml(result.provider)}</p>
            <p><strong>Запрос:</strong> ${escapeHtml(result.prompt)}</p>
            <div class="text-block">${escapeHtml(result.response)}</div>
        `;
        return;
    }

    const timings = Object.entries(result.timings_sec || {})
        .map(([k, v]) => `${k}: ${v} сек`)
        .join(" · ");

    resultContent.innerHTML = `
        <p><strong>Исходный промпт:</strong> ${escapeHtml(result.prompt)}</p>
        <p><strong>Улучшенный промпт:</strong> ${escapeHtml(result.refined_prompt)}</p>
        <img src="${result.image_url}?t=${Date.now()}" alt="Сгенерированное изображение">
        <p class="meta">Время: ${result.total_sec} сек (${escapeHtml(timings)})</p>
    `;
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function stopPolling() {
    if (pollTimer) {
        clearInterval(pollTimer);
        pollTimer = null;
    }
}

function pollStatus(taskId) {
    stopPolling();

    pollTimer = setInterval(async () => {
        try {
            const response = await fetch(`/api/status/${taskId}`);
            const data = await response.json();

            if (!response.ok) {
                stopPolling();
                showError(data.error || "Ошибка получения статуса");
                return;
            }

            showProgress(data.progress || 0, data.message || "Обработка...");

            if (data.status === "completed") {
                stopPolling();
                showResult(data.result);
            } else if (data.status === "error") {
                stopPolling();
                showError(data.message || "Неизвестная ошибка");
            }
        } catch (err) {
            stopPolling();
            showError(`Сетевая ошибка: ${err.message}`);
        }
    }, 1000);
}

async function startGeneration() {
    const prompt = promptInput.value.trim();
    const mode = modeSelect.value;

    if (!prompt) {
        showError("Введите промпт");
        return;
    }

    submitBtn.disabled = true;
    hideAllSections();
    showProgress(0, "Отправка запроса...");

    try {
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt, mode }),
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || "Ошибка запуска");
            return;
        }

        pollStatus(data.task_id);
    } catch (err) {
        showError(`Сетевая ошибка: ${err.message}`);
    }
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    startGeneration();
});

newRequestBtn.addEventListener("click", () => {
    hideAllSections();
    promptInput.focus();
});

retryBtn.addEventListener("click", () => {
    startGeneration();
});
