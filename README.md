# CLI для OpenAI / GigaChat

Интерактивное CLI-приложение на Python для отправки пользовательских запросов в OpenAI или GigaChat.

## Структура проекта

```
.
├── app.py            # Flask веб-интерфейс
├── main.py           # Точка входа CLI
├── pipeline.py       # Мультимодальный пайплайн
├── config.py         # Определение активного провайдера
├── providers.py      # OpenAI, GigaChat, ProxyAPI
├── templates/        # HTML-шаблоны
├── static/           # CSS и JS
├── outputs/          # Результаты генерации
├── requirements.txt
├── .env.example
└── venv/
```

## Flask веб-интерфейс

```bash
python app.py
```

Откройте в браузере: http://127.0.0.1:5000

- Форма с выбором режима (чат / изображение)
- Прогресс-бар с опросом статуса задачи
- Отображение результата на странице

## Быстрый старт

### 1. Создание виртуального окружения

**Windows (PowerShell):**
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка API-ключа

Скопируйте шаблон и укажите ключ:

```bash
cp .env.example .env
```

Отредактируйте `.env` — достаточно одного ключа:

- `OPENAI_API_KEY` — для OpenAI
- `GIGACHAT_API_KEY` — для GigaChat (авторизационный ключ из личного кабинета Sber)

Если заданы оба ключа, используется GigaChat.

### 4. Запуск

```bash
python main.py
```

Введите запрос в консоль и нажмите Enter. Ответ появится ниже.

## Переменные окружения

| Переменная         | Обязательность | Описание                          |
|--------------------|----------------|-----------------------------------|
| `OPENAI_API_KEY`   | Один из двух   | API-ключ OpenAI                   |
| `GIGACHAT_API_KEY` | Один из двух   | Credentials для GigaChat          |
| `OPENAI_MODEL`     | Нет            | Модель OpenAI (по умолчанию `gpt-4o-mini`) |
| `GIGACHAT_MODEL`   | Нет            | Модель GigaChat (по умолчанию `GigaChat`)  |

## Примеры запросов

```
> Привет!
> Что такое Python?
> Напиши функцию сортировки.
```

## Мультимодальный режим (GigaChat + ProxyAPI)

Два этапа в одном пайплайне:
1. **Текст** — GigaChat улучшает промпт для генерации изображения
2. **Изображение** — ProxyAPI (`gpt-image-1`) создаёт картинку

### Настройка

В `.env` добавьте:

```env
GIGACHAT_API_KEY=ваш_ключ
PROXY_API=ваш_ключ_proxyapi
```

### Запуск

```bash
python main.py --mode image
```

### Автотест полного цикла

```bash
python run_multimodal_test.py
```

Результаты сохраняются в `outputs/<timestamp>/`:
- `image.png` — сгенерированное изображение
- `prompt_original.txt` — исходный промпт
- `prompt_refined.txt` — улучшенный промпт
- `metadata.json` — время выполнения каждого этапа

## Обработка ошибок

- Отсутствие ключей в `.env` — сообщение об ошибке конфигурации
- Сбой сети или API — сообщение с описанием исключения
- Пустой ввод — корректный выход без обращения к API
