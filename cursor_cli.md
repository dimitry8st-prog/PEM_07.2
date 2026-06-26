# Создание CLI приложения для генерации изображений
_Exported on 12/3/2025 at 16:50:45 GMT+3 from Cursor (2.1.42)_

---

**User**

Создай CLI приложение на Python для генерации изображений

Оно должно использовать Openai(Ключ в env OPENAI_KEY) для генерации



Сохранять нужно в отдельную директорию

Я ввожу промпт в терминал и ожидаю уведление о готов изображении

---

**Cursor**


Проверяю структуру проекта перед созданием CLI для генерации изображений через OpenAI.



Создаю CLI‑приложение для генерации изображений через OpenAI. Добавляю необходимые файлы.


```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с использованием OpenAI DALL-E
"""

import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по промпту: '{prompt}'...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с использованием OpenAI DALL-E")
    print("=" * 60)
    
    # Получение ключа API
    api_key = get_openai_key()
    client = OpenAI(api_key=api_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    # Генерация изображения
    generate_image(client, prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()

```

```pip-requirements
openai>=1.0.0
requests>=2.31.0

```

```markdown
# Генератор изображений OpenAI

CLI приложение для генерации изображений с использованием OpenAI DALL-E 3.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Установите переменную окружения с ключом OpenAI:
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```

## Использование

Запустите приложение:
```bash
python image_generator.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.

```


Проверяю код на ошибки:



Создано CLI‑приложение для генерации изображений через OpenAI.

## Созданные файлы:

1. **`image_generator.py`** — основной скрипт:
   - Читает ключ API из переменной окружения `OPENAI_KEY`
   - Принимает промпт через терминал
   - Генерирует изображение через DALL-E 3
   - Сохраняет в директорию `generated_images/`
   - Выводит уведомление о готовности

2. **`requirements.txt`** — зависимости проекта

3. **`README.md`** — инструкция по использованию

## Как использовать:

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Установите переменную окружения с ключом OpenAI:
   ```powershell
   $env:OPENAI_KEY="your-api-key-here"
   ```

3. Запустите приложение:
   ```bash
   python image_generator.py
   ```

4. Введите промпт, когда программа попросит.

Приложение сохранит изображение в `generated_images/` и выведет уведомление о готовности с путем к файлу.

```shellscript
   pip install -r requirements.txt
```

```powershell
   $env:OPENAI_KEY="your-api-key-here"
```

```shellscript
   python image_generator.py
```

---

**User**

А как поставить виртуальное окружение?

---

**Cursor**


Добавляю инструкции по созданию и активации виртуального окружения в README.



Обновляю README: добавляю инструкции по созданию и активации виртуального окружения.


```markdown
# Генератор изображений OpenAI

CLI приложение для генерации изображений с использованием OpenAI DALL-E 3.

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом OpenAI:
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```

## Использование

Запустите приложение:
```bash
python image_generator.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Обновил README с инструкциями по виртуальному окружению. Кратко:

## Создание виртуального окружения:

**Для Windows PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Для Windows CMD:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

После активации виртуального окружения вы увидите `(venv)` в начале строки терминала.

**Для деактивации** просто введите:
```bash
deactivate
```

Теперь порядок действий:
1. Создать виртуальное окружение
2. Активировать его
3. Установить зависимости (`pip install -r requirements.txt`)
4. Установить переменную окружения `OPENAI_KEY`
5. Запустить приложение

Это изолирует зависимости проекта от системных пакетов Python.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

```plaintext
python -m venv venv
venv\Scripts\activate.bat
```

```shellscript
deactivate
```

---

**User**

создай второй скрипт, который будет работать через proxyapi(env - PROXY_API)

Вот как генерировать по документаци 

Пример для GPT-Image 1

from openai import OpenAI

import base64

client = OpenAI(

    api_key="<КЛЮЧ>",

    base_url="https://api.proxyapi.ru/openai/v1",

)

prompt = """

Стеклянная бутылка, внутри которой плывет корабль посреди шторма

"""

result = client.images.generate(

    model="gpt-image-1",

    prompt=prompt

)

image_base64 = result.data[0].b64_json

image_bytes = base64.b64decode(image_base64)

with open("image.png", "wb") as f:

    f.write(image_bytes)



---

**Cursor**


Изучаю текущий скрипт, чтобы создать второй для ProxyAPI:



Создаю второй скрипт для ProxyAPI:


```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с использованием ProxyAPI GPT-Image
"""

import os
import sys
import base64
from datetime import datetime
from pathlib import Path
from openai import OpenAI


def get_proxy_api_key():
    """Получает ключ ProxyAPI из переменной окружения"""
    api_key = os.getenv("PROXY_API")
    if not api_key:
        print("Ошибка: Переменная окружения PROXY_API не установлена")
        print("Установите её командой: set PROXY_API=your_key (Windows) или export PROXY_API=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по промпту: '{prompt}'...")
    
    try:
        # Генерация изображения через ProxyAPI
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt
        )
        
        # Получение base64 изображения
        image_base64 = result.data[0].b64_json
        
        # Декодирование base64 в байты
        print("Декодирование изображения...")
        image_bytes = base64.b64decode(image_base64)
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_proxy.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_bytes)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с использованием ProxyAPI GPT-Image")
    print("=" * 60)
    
    # Получение ключа API
    api_key = get_proxy_api_key()
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.proxyapi.ru/openai/v1",
    )
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    # Генерация изображения
    generate_image(client, prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()

```


Обновляю README с информацией о втором скрипте:


```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом OpenAI:
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```

## Использование

Запустите приложение:
```bash
python image_generator.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```

```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Создан второй скрипт `image_generator_proxy.py` для ProxyAPI. Обновлен README с инструкциями для обоих скриптов.

## Что было создано:

1. **`image_generator_proxy.py`** — скрипт для ProxyAPI:
   - Использует переменную окружения `PROXY_API`
   - Подключается к `https://api.proxyapi.ru/openai/v1`
   - Использует модель `gpt-image-1`
   - Обрабатывает base64 изображения (как в документации)
   - Сохраняет в ту же директорию `generated_images/`

2. **Обновлен README.md** — добавлены инструкции для обоих скриптов

## Использование ProxyAPI скрипта:

1. Установите переменную окружения:
   ```powershell
   $env:PROXY_API="your-proxy-api-key"
   ```

2. Запустите скрипт:
   ```bash
   python image_generator_proxy.py
   ```

Оба скрипта сохраняют изображения в одну директорию `generated_images/`. Файлы от ProxyAPI имеют суффикс `_proxy.png` для отличия.

```powershell
   $env:PROXY_API="your-proxy-api-key"
```

```shellscript
   python image_generator_proxy.py
```

---

**User**

Допиши модуль который будет работать через gigachat api для конкретизации промпта



Я ввожу промпт в скрипт -> промпт отправляется к gigachat для добавления конкретики -> отправляется на генерацию в openai

---

**Cursor**


Изучаю текущие скрипты, чтобы создать модуль с GigaChat для улучшения промпта перед генерацией в OpenAI:



Создаю модуль с GigaChat для улучшения промпта перед генерацией в OpenAI:



Создаю скрипт с GigaChat для улучшения промпта:


```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_credentials():
    """Получает учетные данные GigaChat из переменных окружения"""
    client_id = os.getenv("GIGACHAT_CLIENT_ID")
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("Ошибка: Переменные окружения GIGACHAT_CLIENT_ID и GIGACHAT_CLIENT_SECRET не установлены")
        print("Установите их командой:")
        print("  Windows (PowerShell):")
        print("    $env:GIGACHAT_CLIENT_ID='your_client_id'")
        print("    $env:GIGACHAT_CLIENT_SECRET='your_client_secret'")
        print("  Windows (CMD):")
        print("    set GIGACHAT_CLIENT_ID=your_client_id")
        print("    set GIGACHAT_CLIENT_SECRET=your_client_secret")
        print("  Linux/Mac:")
        print("    export GIGACHAT_CLIENT_ID='your_client_id'")
        print("    export GIGACHAT_CLIENT_SECRET='your_client_secret'")
        sys.exit(1)
    
    return client_id, client_secret


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        client_id, client_secret = get_gigachat_credentials()
        
        # Инициализация клиента GigaChat
        client = GigaChat(
            client_id=client_id,
            client_secret=client_secret,
            scope="GIGACHAT_API_PERS"
        )
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Отправка запроса и получение ответа
        response = client.chat_completions(
            model="GigaChat-Pro",
            messages=messages,
            temperature=0.7
        )
        
        # Извлечение улучшенного промпта из ответа
        refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    client_id, client_secret = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()

```


Добавляю зависимость `gigachat` в `requirements.txt` и обновляю README:


```pip-requirements
openai>=1.0.0
requests>=2.31.0
python-dotenv>=1.0.0
gigachat>=0.1.0

```


Обновляю README с информацией о новом скрипте:


```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```

```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_CLIENT_ID="your-client-id"
     $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_CLIENT_ID=your-client-id
     set GIGACHAT_CLIENT_SECRET=your-client-secret
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_CLIENT_ID='your-client-id'
     export GIGACHAT_CLIENT_SECRET='your-client-secret'
     export OPENAI_KEY='your-openai-key'
     ```

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

Введите промпт для генерации изображения, когда программа попросит.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```

```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_CLIENT_ID="your-client-id"
     $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_CLIENT_ID=your-client-id
     set GIGACHAT_CLIENT_SECRET=your-client-secret
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_CLIENT_ID='your-client-id'
     export GIGACHAT_CLIENT_SECRET='your-client-secret'
     export OPENAI_KEY='your-openai-key'
     ```

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

Введите промпт для генерации изображения, когда программа попросит. 

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Создан модуль `image_generator_gigachat.py`, который использует GigaChat для улучшения промпта перед генерацией изображения через OpenAI.

## Что было создано:

1. **`image_generator_gigachat.py`** — новый скрипт:
   - Принимает промпт от пользователя
   - Отправляет его в GigaChat API для улучшения и конкретизации
   - Показывает исходный и улучшенный промпты
   - Генерирует изображение через OpenAI DALL-E 3 с улучшенным промптом
   - Сохраняет изображение в `generated_images/` с суффиксом `_gigachat.png`

2. **Обновлен `requirements.txt`** — добавлена библиотека `gigachat`

3. **Обновлен `README.md`** — добавлены инструкции для нового скрипта

## Как использовать:

1. Установите зависимости (если еще не установлены):
   ```bash
   pip install -r requirements.txt
   ```

2. Установите переменные окружения:
   ```powershell
   $env:GIGACHAT_CLIENT_ID="your-client-id"
   $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
   $env:OPENAI_KEY="your-openai-key"
   ```

3. Запустите скрипт:
   ```bash
   python image_generator_gigachat.py
   ```

4. Введите промпт — скрипт покажет улучшенную версию и сгенерирует изображение.

Скрипт автоматически улучшает промпт через GigaChat, добавляя детали о стиле, композиции, освещении и цветовой палитре для лучших результатов генерации.

```shellscript
   pip install -r requirements.txt
```

```powershell
   $env:GIGACHAT_CLIENT_ID="your-client-id"
   $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
   $env:OPENAI_KEY="your-openai-key"
```

```shellscript
   python image_generator_gigachat.py
```

---

**User**

Исправь код, вот документаци:

https://developers.sber.ru/docs/ru/gigachain/tools/python/gigachat?ysclid=miq179qxkv74470296 



Вот ошибка:

@python (8-20) 

---

**Cursor**


Изучаю документацию и текущий код, чтобы исправить работу с GigaChat API:



Исправляю код согласно документации GigaChat API:


```python
def get_gigachat_credentials():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY (новый формат)
    api_key = os.getenv("GIGACHAT_API_KEY")
    if api_key:
        return api_key
    
    # Проверяем старый формат с client_id и client_secret
    client_id = os.getenv("GIGACHAT_CLIENT_ID")
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    
    if not api_key and (not client_id or not client_secret):
        print("Ошибка: Переменная окружения GIGACHAT_API_KEY не установлена")
        print("Установите её командой:")
        print("  Windows (PowerShell):")
        print("    $env:GIGACHAT_API_KEY='your-api-key'")
        print("  Windows (CMD):")
        print("    set GIGACHAT_API_KEY=your-api-key")
        print("  Linux/Mac:")
        print("    export GIGACHAT_API_KEY='your-api-key'")
        print("\nИли используйте старый формат:")
        print("  GIGACHAT_CLIENT_ID и GIGACHAT_CLIENT_SECRET")
        sys.exit(1)
    
    # Если используется старый формат, возвращаем client_secret как credentials
    if client_secret:
        return client_secret
    
    return api_key
```

```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_credentials():
    """Получает учетные данные GigaChat из переменных окружения"""
    client_id = os.getenv("GIGACHAT_CLIENT_ID")
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("Ошибка: Переменные окружения GIGACHAT_CLIENT_ID и GIGACHAT_CLIENT_SECRET не установлены")
        print("Установите их командой:")
        print("  Windows (PowerShell):")
        print("    $env:GIGACHAT_CLIENT_ID='your_client_id'")
        print("    $env:GIGACHAT_CLIENT_SECRET='your_client_secret'")
        print("  Windows (CMD):")
        print("    set GIGACHAT_CLIENT_ID=your_client_id")
        print("    set GIGACHAT_CLIENT_SECRET=your_client_secret")
        print("  Linux/Mac:")
        print("    export GIGACHAT_CLIENT_ID='your_client_id'")
        print("    export GIGACHAT_CLIENT_SECRET='your_client_secret'")
        sys.exit(1)
    
    return client_id, client_secret


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        credentials = get_gigachat_credentials()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # Формируем полный запрос с системным сообщением
        full_message = f"{system_message}\n\n{user_message}"
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Инициализация и использование GigaChat клиента
        with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(full_message)
            refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    client_id, client_secret = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```

```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_credentials():
    """Получает учетные данные GigaChat из переменных окружения"""
    client_id = os.getenv("GIGACHAT_CLIENT_ID")
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("Ошибка: Переменные окружения GIGACHAT_CLIENT_ID и GIGACHAT_CLIENT_SECRET не установлены")
        print("Установите их командой:")
        print("  Windows (PowerShell):")
        print("    $env:GIGACHAT_CLIENT_ID='your_client_id'")
        print("    $env:GIGACHAT_CLIENT_SECRET='your_client_secret'")
        print("  Windows (CMD):")
        print("    set GIGACHAT_CLIENT_ID=your_client_id")
        print("    set GIGACHAT_CLIENT_SECRET=your_client_secret")
        print("  Linux/Mac:")
        print("    export GIGACHAT_CLIENT_ID='your_client_id'")
        print("    export GIGACHAT_CLIENT_SECRET='your_client_secret'")
        sys.exit(1)
    
    return client_id, client_secret


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        credentials = get_gigachat_credentials()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # Формируем полный запрос с системным сообщением
        full_message = f"{system_message}\n\n{user_message}"
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Инициализация и использование GigaChat клиента
        with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(full_message)
            refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    gigachat_credentials = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```


Читаю файл, чтобы исправить функцию `get_gigachat_credentials`:



Исправляю функцию `get_gigachat_credentials()`: она должна возвращать строку credentials, а не кортеж.


```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_credentials():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY (новый формат)
    api_key = os.getenv("GIGACHAT_API_KEY")
    if api_key:
        return api_key
    
    # Проверяем старый формат с client_secret (обычно используется client_secret как credentials)
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    if client_secret:
        return client_secret
    
    # Если ничего не найдено
    print("Ошибка: Переменная окружения GIGACHAT_API_KEY или GIGACHAT_CLIENT_SECRET не установлена")
    print("Установите её командой:")
    print("  Windows (PowerShell):")
    print("    $env:GIGACHAT_API_KEY='your-api-key'")
    print("  Windows (CMD):")
    print("    set GIGACHAT_API_KEY=your-api-key")
    print("  Linux/Mac:")
    print("    export GIGACHAT_API_KEY='your-api-key'")
    print("\nИли используйте старый формат:")
    print("  set GIGACHAT_CLIENT_SECRET=your-client-secret")
    sys.exit(1)


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        credentials = get_gigachat_credentials()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # Формируем полный запрос с системным сообщением
        full_message = f"{system_message}\n\n{user_message}"
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Инициализация и использование GigaChat клиента
        with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(full_message)
            refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    gigachat_credentials = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```


Обновляю README с информацией о переменных окружения:



Обновляю README с правильными переменными окружения:


```markdown
# Генератор изображений

CLI приложения для генерации изображений:
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_API_KEY="your-api-key"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_API_KEY=your-api-key
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_API_KEY='your-api-key'
     export OPENAI_KEY='your-openai-key'
     ```
   
   *Примечание: Также можно использовать `GIGACHAT_CLIENT_SECRET` вместо `GIGACHAT_API_KEY`*

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

Введите промпт для генерации изображения, когда программа попросит. 

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Исправлен код для работы с GigaChat API. Изменения:

## Исправления:

1. **Функция `get_gigachat_credentials()`** — теперь возвращает строку с ключом авторизации (поддерживает `GIGACHAT_API_KEY` или `GIGACHAT_CLIENT_SECRET`)

2. **Функция `refine_prompt_with_gigachat()`** — исправлена инициализация клиента GigaChat:
   - Используется правильный формат `GigaChat(credentials=credentials, verify_ssl_certs=False)`
   - Используется метод `chat()` для отправки сообщения
   - Формируется полное сообщение с системным промптом и пользовательским запросом

3. **Обновлен README** — добавлена информация о переменной `GIGACHAT_API_KEY`

## Как использовать:

1. Установите переменную окружения:
   ```powershell
   $env:GIGACHAT_API_KEY="your-api-key"
   $env:OPENAI_KEY="your-openai-key"
   ```

2. Запустите скрипт:
   ```bash
   python image_generator_gigachat.py
   ```

Код должен работать корректно. GigaChat улучшит промпт, добавив детали о стиле, композиции и освещении, а затем улучшенный промпт будет использован для генерации изображения через OpenAI DALL-E 3.

```powershell
   $env:GIGACHAT_API_KEY="your-api-key"
   $env:OPENAI_KEY="your-openai-key"
```

```shellscript
   python image_generator_gigachat.py
```

---

**User**

Перепиши использование gigachat, используй простые requests запросы

---

**Cursor**


Изучаю текущий код и документацию GigaChat API, чтобы переписать использование на простые HTTP-запросы через `requests`:



Переписываю код для использования простых HTTP-запросов через `requests`:


```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_credentials():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY (новый формат)
    api_key = os.getenv("GIGACHAT_API_KEY")
    if api_key:
        return api_key
    
    # Проверяем старый формат с client_secret (обычно используется client_secret как credentials)
    client_secret = os.getenv("GIGACHAT_CLIENT_SECRET")
    if client_secret:
        return client_secret
    
    # Если ничего не найдено
    print("Ошибка: Переменная окружения GIGACHAT_API_KEY или GIGACHAT_CLIENT_SECRET не установлена")
    print("Установите её командой:")
    print("  Windows (PowerShell):")
    print("    $env:GIGACHAT_API_KEY='your-api-key'")
    print("  Windows (CMD):")
    print("    set GIGACHAT_API_KEY=your-api-key")
    print("  Linux/Mac:")
    print("    export GIGACHAT_API_KEY='your-api-key'")
    print("\nИли используйте старый формат:")
    print("  set GIGACHAT_CLIENT_SECRET=your-client-secret")
    sys.exit(1)


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        credentials = get_gigachat_credentials()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # Формируем полный запрос с системным сообщением
        full_message = f"{system_message}\n\n{user_message}"
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Инициализация и использование GigaChat клиента
        with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(full_message)
            refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    gigachat_credentials = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```

```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY
    auth_key = os.getenv("GIGACHAT_API_KEY")
    if auth_key:
        return auth_key
    
    # Если ничего не найдено
    print("Ошибка: Переменная окружения GIGACHAT_API_KEY не установлена")
    print("Установите её командой:")
    print("  Windows (PowerShell):")
    print("    $env:GIGACHAT_API_KEY='your-api-key'")
    print("  Windows (CMD):")
    print("    set GIGACHAT_API_KEY=your-api-key")
    print("  Linux/Mac:")
    print("    export GIGACHAT_API_KEY='your-api-key'")
    sys.exit(1)


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        print(f"\n✗ Ошибка при получении токена доступа GigaChat: {str(e)}")
        raise


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API"""
    try:
        from gigachat import GigaChat
        
        credentials = get_gigachat_credentials()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # Формируем полный запрос с системным сообщением
        full_message = f"{system_message}\n\n{user_message}"
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Инициализация и использование GigaChat клиента
        with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(full_message)
            refined_prompt = response.choices[0].message.content.strip()
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except ImportError:
        print("Ошибка: Библиотека gigachat не установлена")
        print("Установите её командой: pip install gigachat")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    gigachat_credentials = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```

```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY
    auth_key = os.getenv("GIGACHAT_API_KEY")
    if auth_key:
        return auth_key
    
    # Если ничего не найдено
    print("Ошибка: Переменная окружения GIGACHAT_API_KEY не установлена")
    print("Установите её командой:")
    print("  Windows (PowerShell):")
    print("    $env:GIGACHAT_API_KEY='your-api-key'")
    print("  Windows (CMD):")
    print("    set GIGACHAT_API_KEY=your-api-key")
    print("  Linux/Mac:")
    print("    export GIGACHAT_API_KEY='your-api-key'")
    sys.exit(1)


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        print(f"\n✗ Ошибка при получении токена доступа GigaChat: {str(e)}")
        raise


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API через HTTP запросы"""
    try:
        # Получаем токен доступа
        access_token = get_gigachat_access_token()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # URL для отправки запроса к GigaChat API
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            'model': 'GigaChat',
            'messages': [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        }
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Отправка запроса
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        # Обработка ответа
        response_data = response.json()
        choices = response_data.get('choices', [])
        if choices:
            refined_prompt = choices[0].get('message', {}).get('content', '').strip()
        else:
            raise ValueError("Пустой ответ от GigaChat API")
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    gigachat_credentials = get_gigachat_credentials()
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```

```python
#!/usr/bin/env python3
"""
CLI приложение для генерации изображений с улучшением промпта через GigaChat
Поток: Пользователь -> GigaChat (улучшение промпта) -> OpenAI (генерация изображения)
"""

import os
import sys
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    # Проверяем GIGACHAT_API_KEY
    auth_key = os.getenv("GIGACHAT_API_KEY")
    if auth_key:
        return auth_key
    
    # Если ничего не найдено
    print("Ошибка: Переменная окружения GIGACHAT_API_KEY не установлена")
    print("Установите её командой:")
    print("  Windows (PowerShell):")
    print("    $env:GIGACHAT_API_KEY='your-api-key'")
    print("  Windows (CMD):")
    print("    set GIGACHAT_API_KEY=your-api-key")
    print("  Linux/Mac:")
    print("    export GIGACHAT_API_KEY='your-api-key'")
    sys.exit(1)


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        print(f"\n✗ Ошибка при получении токена доступа GigaChat: {str(e)}")
        raise


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Ошибка: Переменная окружения OPENAI_KEY не установлена")
        print("Установите её командой: set OPENAI_KEY=your_key (Windows) или export OPENAI_KEY=your_key (Linux/Mac)")
        sys.exit(1)
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API через HTTP запросы"""
    try:
        # Получаем токен доступа
        access_token = get_gigachat_access_token()
        
        # Формирование запроса для улучшения промпта
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        # URL для отправки запроса к GigaChat API
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            'model': 'GigaChat',
            'messages': [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        }
        
        print("\nОтправка промпта в GigaChat для улучшения...")
        
        # Отправка запроса
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        # Обработка ответа
        response_data = response.json()
        choices = response_data.get('choices', [])
        if choices:
            refined_prompt = choices[0].get('message', {}).get('content', '').strip()
        else:
            raise ValueError("Пустой ответ от GigaChat API")
        
        # Убираем возможные кавычки и лишние символы
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        
        return refined_prompt
        
    except Exception as e:
        print(f"\n✗ Ошибка при улучшении промпта через GigaChat: {str(e)}")
        print("Используется исходный промпт...")
        return prompt


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(client, prompt, output_dir):
    """Генерирует изображение по промпту и сохраняет его"""
    print(f"\nГенерация изображения по улучшенному промпту...")
    
    try:
        # Генерация изображения через OpenAI API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Получение URL изображения
        image_url = response.data[0].url
        
        # Скачивание изображения
        print("Скачивание изображения...")
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла с временной меткой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_gigachat.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        print(f"\n✓ Изображение успешно сохранено: {filepath}")
        print(f"  URL: {image_url}")
        return filepath
        
    except Exception as e:
        print(f"\n✗ Ошибка при генерации изображения: {str(e)}")
        sys.exit(1)


def main():
    """Основная функция CLI приложения"""
    print("=" * 60)
    print("Генератор изображений с улучшением промпта через GigaChat")
    print("=" * 60)
    
    # Получение ключей API
    openai_key = get_openai_key()
    
    # Инициализация клиентов
    openai_client = OpenAI(api_key=openai_key)
    
    # Создание директории для сохранения
    output_dir = create_output_directory()
    print(f"\nИзображения будут сохранены в: {output_dir.absolute()}")
    
    # Получение промпта от пользователя
    print("\n" + "-" * 60)
    original_prompt = input("Введите промпт для генерации изображения: ").strip()
    
    if not original_prompt:
        print("Ошибка: Промпт не может быть пустым")
        sys.exit(1)
    
    print(f"\nИсходный промпт: {original_prompt}")
    
    # Улучшение промпта через GigaChat
    refined_prompt = refine_prompt_with_gigachat(original_prompt)
    
    print(f"\nУлучшенный промпт: {refined_prompt}")
    print("-" * 60)
    
    # Генерация изображения с улучшенным промптом
    generate_image(openai_client, refined_prompt, output_dir)
    
    print("\n" + "=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()


```


Удаляю зависимость `gigachat` из `requirements.txt`, так как она больше не нужна:


```pip-requirements
openai>=1.0.0
requests>=2.31.0
python-dotenv>=1.0.0

```


Проверяю финальную версию кода:



Код переписан для использования простых HTTP-запросов через `requests`. Изменения:

## Изменения:

1. Удалена зависимость от библиотеки `gigachat` — теперь используются только стандартные HTTP-запросы через `requests`.

2. Добавлена функция `get_gigachat_access_token()` — получает токен доступа через OAuth endpoint GigaChat.

3. Переписана функция `refine_prompt_with_gigachat()` — теперь использует прямые HTTP-запросы:
   - Сначала получает токен доступа через OAuth
   - Затем отправляет запрос к API чата GigaChat
   - Обрабатывает JSON-ответ

4. Обновлен `requirements.txt` — удалена зависимость `gigachat`.

5. Добавлен импорт `uuid` — для генерации уникального RqUID в OAuth запросе.

## Как работает:

1. Получение токена: отправляется POST-запрос к OAuth endpoint с ключом авторизации.
2. Улучшение промпта: используется полученный токен для отправки запроса к API чата.
3. Обработка ответа: извлекается улучшенный промпт из JSON-ответа.

Код теперь использует только стандартные библиотеки (`requests`, `uuid`) без дополнительных зависимостей.

---

**User**

Напиши сайт на flask, через него я могу отправлять запросы на генерацию фото, и оттуда же смотреть результат



Должны быть:

1. Поле для промпта

2. Выбор стиля(промпты длоя стилей пропиши заранее)

3. Доработка промпта через gigachat

4. Отображение прогресс бара

5. возможность делать новые запросы

---

**Cursor**


Создаю Flask-приложение для генерации изображений с указанным функционалом. Изучаю текущую структуру проекта:



Создаю Flask-приложение с указанным функционалом:



Создаю Flask-приложение и необходимые файлы:


```python
"""
Утилиты для генерации изображений
"""

import os
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# Предопределенные стили промптов
STYLE_PROMPTS = {
    "realistic": "photorealistic, highly detailed, professional photography, sharp focus, 8k resolution",
    "anime": "anime style, vibrant colors, detailed character design, Japanese animation style, high quality",
    "cyberpunk": "cyberpunk aesthetic, neon lights, futuristic cityscape, dark atmosphere, sci-fi elements",
    "fantasy": "fantasy art style, magical atmosphere, epic composition, detailed fantasy elements, mystical lighting",
    "watercolor": "watercolor painting style, soft colors, artistic brushstrokes, dreamy atmosphere, artistic",
    "oil_painting": "oil painting style, classical art, rich colors, detailed brushwork, museum quality",
    "sketch": "pencil sketch style, black and white, detailed linework, artistic drawing, monochrome",
    "3d_render": "3D render, CGI, computer graphics, highly detailed, professional 3D modeling, realistic lighting",
    "vintage": "vintage style, retro aesthetic, aged look, classic photography, nostalgic atmosphere",
    "minimalist": "minimalist style, clean composition, simple design, modern aesthetic, elegant simplicity"
}


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    auth_key = os.getenv("GIGACHAT_CLIENT_SECRET")
    if not auth_key:
        raise ValueError("Переменная окружения GIGACHAT_CLIENT_SECRET не установлена")
    return auth_key


def get_gigachat_rquid():
    """Получает RqUID для запроса к GigaChat API"""
    rquid = os.getenv("GIGACHAT_CLIENT_ID")
    if not rquid:
        rquid = str(uuid.uuid4())  # Используем UUID если не задан
    return rquid


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    rquid = get_gigachat_rquid()

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rquid,
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        raise Exception(f"Ошибка при получении токена доступа GigaChat: {str(e)}")


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        raise ValueError("Переменная окружения OPENAI_KEY не установлена")
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API через HTTP запросы"""
    try:
        access_token = get_gigachat_access_token()
        
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            'model': 'GigaChat',
            'messages': [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        }
        
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        response_data = response.json()
        choices = response_data.get('choices', [])
        if choices:
            refined_prompt = choices[0].get('message', {}).get('content', '').strip()
        else:
            raise ValueError("Пустой ответ от GigaChat API")
        
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        return refined_prompt
        
    except Exception as e:
        raise Exception(f"Ошибка при улучшении промпта через GigaChat: {str(e)}")


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(prompt, style=None):
    """Генерирует изображение по промпту и сохраняет его"""
    try:
        # Добавляем стиль к промпту если указан
        if style and style in STYLE_PROMPTS:
            prompt = f"{prompt}, {STYLE_PROMPTS[style]}"
        
        api_key = get_openai_key()
        client = OpenAI(api_key=api_key)
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Скачивание изображения
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла
        output_dir = create_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        return {
            'filepath': str(filepath),
            'filename': filename,
            'url': image_url,
            'prompt': prompt
        }
        
    except Exception as e:
        raise Exception(f"Ошибка при генерации изображения: {str(e)}")

```

```python
"""
Flask веб-приложение для генерации изображений
"""

import os
import threading
import time
from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path
from image_generator_utils import (
    refine_prompt_with_gigachat,
    generate_image,
    STYLE_PROMPTS
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Хранилище статусов задач
tasks_status = {}


def process_generation_task(task_id, prompt, style, use_gigachat):
    """Обрабатывает задачу генерации изображения в отдельном потоке"""
    try:
        tasks_status[task_id] = {'status': 'processing', 'progress': 10, 'message': 'Начало обработки...'}
        
        final_prompt = prompt
        
        # Улучшение промпта через GigaChat
        if use_gigachat:
            tasks_status[task_id] = {'status': 'processing', 'progress': 30, 'message': 'Улучшение промпта через GigaChat...'}
            try:
                refined = refine_prompt_with_gigachat(prompt)
                final_prompt = refined
                tasks_status[task_id] = {'status': 'processing', 'progress': 50, 'message': 'Промпт улучшен, генерация изображения...'}
            except Exception as e:
                tasks_status[task_id] = {'status': 'processing', 'progress': 40, 'message': f'Ошибка улучшения промпта: {str(e)}, используем исходный промпт'}
        else:
            tasks_status[task_id] = {'status': 'processing', 'progress': 40, 'message': 'Генерация изображения...'}
        
        # Генерация изображения
        tasks_status[task_id] = {'status': 'processing', 'progress': 60, 'message': 'Генерация изображения через OpenAI...'}
        result = generate_image(final_prompt, style)
        
        tasks_status[task_id] = {
            'status': 'completed',
            'progress': 100,
            'message': 'Готово!',
            'result': result
        }
        
    except Exception as e:
        tasks_status[task_id] = {
            'status': 'error',
            'progress': 0,
            'message': f'Ошибка: {str(e)}'
        }


@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', styles=STYLE_PROMPTS.keys())


@app.route('/api/generate', methods=['POST'])
def api_generate():
    """API endpoint для запуска генерации изображения"""
    data = request.json
    prompt = data.get('prompt', '').strip()
    style = data.get('style', '')
    use_gigachat = data.get('use_gigachat', False)
    
    if not prompt:
        return jsonify({'error': 'Промпт не может быть пустым'}), 400
    
    # Создаем уникальный ID задачи
    task_id = f"task_{int(time.time() * 1000)}"
    
    # Инициализируем статус задачи
    tasks_status[task_id] = {'status': 'queued', 'progress': 0, 'message': 'Задача поставлена в очередь...'}
    
    # Запускаем генерацию в отдельном потоке
    thread = threading.Thread(
        target=process_generation_task,
        args=(task_id, prompt, style, use_gigachat)
    )
    thread.daemon = True
    thread.start()
    
    return jsonify({'task_id': task_id})


@app.route('/api/status/<task_id>')
def api_status(task_id):
    """API endpoint для проверки статуса задачи"""
    if task_id not in tasks_status:
        return jsonify({'error': 'Задача не найдена'}), 404
    
    return jsonify(tasks_status[task_id])


@app.route('/generated_images/<filename>')
def serve_image(filename):
    """Отдает сгенерированные изображения"""
    return send_from_directory('generated_images', filename)


@app.route('/api/styles')
def api_styles():
    """API endpoint для получения списка стилей"""
    return jsonify({'styles': list(STYLE_PROMPTS.keys())})


if __name__ == '__main__':
    # Создаем директорию для изображений если её нет
    Path('generated_images').mkdir(exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

```


Создаю директории для Windows:



Создаю HTML-шаблоны и статические файлы:


```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Генератор изображений</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <header>
            <h1>🎨 Генератор изображений</h1>
            <p class="subtitle">Создавайте уникальные изображения с помощью AI</p>
        </header>

        <main>
            <div class="form-container">
                <form id="generateForm">
                    <div class="form-group">
                        <label for="prompt">Описание изображения:</label>
                        <textarea 
                            id="prompt" 
                            name="prompt" 
                            rows="4" 
                            placeholder="Введите описание того, что вы хотите увидеть на изображении..."
                            required
                        ></textarea>
                    </div>

                    <div class="form-group">
                        <label for="style">Стиль изображения:</label>
                        <select id="style" name="style">
                            <option value="">Без стиля</option>
                            <option value="realistic">Реалистичный</option>
                            <option value="anime">Аниме</option>
                            <option value="cyberpunk">Киберпанк</option>
                            <option value="fantasy">Фэнтези</option>
                            <option value="watercolor">Акварель</option>
                            <option value="oil_painting">Масляная живопись</option>
                            <option value="sketch">Эскиз</option>
                            <option value="3d_render">3D рендер</option>
                            <option value="vintage">Винтаж</option>
                            <option value="minimalist">Минимализм</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label class="checkbox-label">
                            <input type="checkbox" id="use_gigachat" name="use_gigachat" checked>
                            <span>Улучшить промпт через GigaChat</span>
                        </label>
                    </div>

                    <button type="submit" id="generateBtn" class="btn-primary">
                        Сгенерировать изображение
                    </button>
                </form>
            </div>

            <!-- Прогресс бар -->
            <div id="progressContainer" class="progress-container" style="display: none;">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar">
                        <div id="progressBar" class="progress-bar-fill"></div>
                    </div>
                    <div id="progressText" class="progress-text">0%</div>
                </div>
                <div id="progressMessage" class="progress-message"></div>
            </div>

            <!-- Результат -->
            <div id="resultContainer" class="result-container" style="display: none;">
                <h2>Результат:</h2>
                <div id="resultContent" class="result-content">
                    <!-- Здесь будет отображаться изображение -->
                </div>
                <div class="result-actions">
                    <button id="newRequestBtn" class="btn-secondary">Создать новый запрос</button>
                </div>
            </div>

            <!-- Ошибка -->
            <div id="errorContainer" class="error-container" style="display: none;">
                <div class="error-message">
                    <span id="errorText"></span>
                </div>
                <button id="closeErrorBtn" class="btn-secondary">Закрыть</button>
            </div>
        </main>
    </div>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>

```

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    overflow: hidden;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px 30px;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    font-weight: 700;
}

.subtitle {
    font-size: 1.1em;
    opacity: 0.9;
}

main {
    padding: 40px 30px;
}

.form-container {
    margin-bottom: 30px;
}

.form-group {
    margin-bottom: 25px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #555;
    font-size: 1em;
}

textarea,
select {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1em;
    font-family: inherit;
    transition: border-color 0.3s;
}

textarea:focus,
select:focus {
    outline: none;
    border-color: #667eea;
}

textarea {
    resize: vertical;
    min-height: 100px;
}

.checkbox-label {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-weight: normal;
}

.checkbox-label input[type="checkbox"] {
    width: auto;
    margin-right: 10px;
    cursor: pointer;
    transform: scale(1.2);
}

.btn-primary,
.btn-secondary {
    padding: 15px 30px;
    border: none;
    border-radius: 10px;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    width: 100%;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-primary:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
}

.btn-primary:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.btn-secondary {
    background: #f0f0f0;
    color: #333;
    margin-top: 15px;
}

.btn-secondary:hover {
    background: #e0e0e0;
}

/* Прогресс бар */
.progress-container {
    margin: 30px 0;
    padding: 25px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.progress-bar-wrapper {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.progress-bar {
    flex: 1;
    height: 30px;
    background: #e0e0e0;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
}

.progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    transition: width 0.3s ease;
    width: 0%;
    position: relative;
    overflow: hidden;
}

.progress-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.3),
        transparent
    );
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(100%);
    }
}

.progress-text {
    font-weight: 600;
    font-size: 1.1em;
    color: #667eea;
    min-width: 50px;
    text-align: right;
}

.progress-message {
    color: #666;
    font-size: 0.95em;
    text-align: center;
}

/* Результат */
.result-container {
    margin: 30px 0;
    padding: 30px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.result-container h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 1.8em;
}

.result-content {
    text-align: center;
}

.result-content img {
    max-width: 100%;
    height: auto;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}

.result-info {
    margin-top: 20px;
    padding: 15px;
    background: white;
    border-radius: 10px;
    text-align: left;
}

.result-info p {
    margin: 10px 0;
    color: #666;
}

.result-info strong {
    color: #333;
}

.result-actions {
    margin-top: 20px;
}

/* Ошибка */
.error-container {
    margin: 30px 0;
    padding: 25px;
    background: #fff5f5;
    border: 2px solid #fc8181;
    border-radius: 15px;
}

.error-message {
    color: #c53030;
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 1.1em;
}

/* Анимации */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.result-container,
.progress-container,
.error-container {
    animation: fadeIn 0.5s ease;
}

/* Адаптивность */
@media (max-width: 768px) {
    header h1 {
        font-size: 2em;
    }

    main {
        padding: 20px;
    }

    .progress-bar-wrapper {
        flex-direction: column;
        gap: 10px;
    }

    .progress-text {
        text-align: center;
    }
}

```

```javascript
// Обработка формы генерации
document.getElementById('generateForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const prompt = document.getElementById('prompt').value.trim();
    const style = document.getElementById('style').value;
    const useGigachat = document.getElementById('use_gigachat').checked;
    
    if (!prompt) {
        showError('Пожалуйста, введите описание изображения');
        return;
    }
    
    // Скрываем предыдущие результаты и ошибки
    hideResult();
    hideError();
    
    // Показываем прогресс бар
    showProgress();
    
    // Отправляем запрос на генерацию
    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt: prompt,
                style: style,
                use_gigachat: useGigachat
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Ошибка при отправке запроса');
        }
        
        const data = await response.json();
        const taskId = data.task_id;
        
        // Начинаем отслеживание статуса
        pollStatus(taskId);
        
    } catch (error) {
        hideProgress();
        showError(error.message);
    }
});

// Функция для опроса статуса задачи
async function pollStatus(taskId) {
    const maxAttempts = 300; // Максимум 5 минут (300 * 1 секунда)
    let attempts = 0;
    
    const interval = setInterval(async () => {
        attempts++;
        
        try {
            const response = await fetch(`/api/status/${taskId}`);
            
            if (!response.ok) {
                throw new Error('Ошибка при проверке статуса');
            }
            
            const status = await response.json();
            
            // Обновляем прогресс бар
            updateProgress(status.progress, status.message);
            
            if (status.status === 'completed') {
                clearInterval(interval);
                hideProgress();
                showResult(status.result);
            } else if (status.status === 'error') {
                clearInterval(interval);
                hideProgress();
                showError(status.message);
            } else if (attempts >= maxAttempts) {
                clearInterval(interval);
                hideProgress();
                showError('Превышено время ожидания. Попробуйте еще раз.');
            }
            
        } catch (error) {
            clearInterval(interval);
            hideProgress();
            showError(error.message);
        }
    }, 1000); // Проверяем каждую секунду
}

// Функции для управления UI
function showProgress() {
    document.getElementById('progressContainer').style.display = 'block';
    document.getElementById('generateBtn').disabled = true;
    updateProgress(0, 'Инициализация...');
}

function hideProgress() {
    document.getElementById('progressContainer').style.display = 'none';
    document.getElementById('generateBtn').disabled = false;
}

function updateProgress(percent, message) {
    document.getElementById('progressBar').style.width = percent + '%';
    document.getElementById('progressText').textContent = percent + '%';
    document.getElementById('progressMessage').textContent = message;
}

function showResult(result) {
    const container = document.getElementById('resultContainer');
    const content = document.getElementById('resultContent');
    
    content.innerHTML = `
        <img src="/generated_images/${result.filename}" alt="Generated image">
        <div class="result-info">
            <p><strong>Промпт:</strong> ${escapeHtml(result.prompt)}</p>
            <p><strong>Файл:</strong> ${result.filename}</p>
        </div>
    `;
    
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideResult() {
    document.getElementById('resultContainer').style.display = 'none';
}

function showError(message) {
    const container = document.getElementById('errorContainer');
    const errorText = document.getElementById('errorText');
    
    errorText.textContent = message;
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
    document.getElementById('errorContainer').style.display = 'none';
}

// Обработчик кнопки "Создать новый запрос"
document.getElementById('newRequestBtn').addEventListener('click', () => {
    hideResult();
    hideError();
    document.getElementById('prompt').value = '';
    document.getElementById('style').value = '';
    document.getElementById('prompt').focus();
});

// Обработчик кнопки закрытия ошибки
document.getElementById('closeErrorBtn').addEventListener('click', () => {
    hideError();
});

// Функция для экранирования HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

```

```pip-requirements
openai>=1.0.0
requests>=2.31.0
python-dotenv>=1.0.0
flask>=3.0.0

```


Обновляю README с инструкциями по запуску веб-приложения:



Добавляю информацию о веб-приложении в README:


```markdown
# Генератор изображений

Приложения для генерации изображений:

**CLI приложения:**
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

**Веб-приложение:**
- **app.py** - Flask веб-интерфейс с выбором стилей, улучшением промпта через GigaChat и прогресс-баром

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_API_KEY="your-api-key"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_API_KEY=your-api-key
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_API_KEY='your-api-key'
     export OPENAI_KEY='your-openai-key'
     ```
   
   *Примечание: Также можно использовать `GIGACHAT_CLIENT_SECRET` вместо `GIGACHAT_API_KEY`*

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

Введите промпт для генерации изображения, когда программа попросит. 

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```

```markdown
# Генератор изображений

Приложения для генерации изображений:

**CLI приложения:**
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

**Веб-приложение:**
- **app.py** - Flask веб-интерфейс с выбором стилей, улучшением промпта через GigaChat и прогресс-баром

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py и app.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_CLIENT_ID="your-client-id"
     $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_CLIENT_ID=your-client-id
     set GIGACHAT_CLIENT_SECRET=your-client-secret
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_CLIENT_ID='your-client-id'
     export GIGACHAT_CLIENT_SECRET='your-client-secret'
     export OPENAI_KEY='your-openai-key'
     ```
   
   *Примечание: Для веб-приложения требуются все три переменные окружения*

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

Введите промпт для генерации изображения, когда программа попросит. 

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```

```markdown
# Генератор изображений

Приложения для генерации изображений:

**CLI приложения:**
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

**Веб-приложение:**
- **app.py** - Flask веб-интерфейс с выбором стилей, улучшением промпта через GigaChat и прогресс-баром

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py и app.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_CLIENT_ID="your-client-id"
     $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_CLIENT_ID=your-client-id
     set GIGACHAT_CLIENT_SECRET=your-client-secret
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_CLIENT_ID='your-client-id'
     export GIGACHAT_CLIENT_SECRET='your-client-secret'
     export OPENAI_KEY='your-openai-key'
     ```
   
   *Примечание: Для веб-приложения требуются все три переменные окружения*

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

**Веб-приложение Flask:**
```bash
python app.py
```

Затем откройте браузер и перейдите по адресу: `http://localhost:5000`

**Возможности веб-приложения:**
- Поле для ввода промпта
- Выбор стиля изображения (10 предустановленных стилей)
- Опция улучшения промпта через GigaChat
- Прогресс-бар с отображением статуса генерации
- Просмотр результатов прямо в браузере
- Возможность создавать новые запросы

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Создано Flask веб-приложение для генерации изображений. Реализовано:

## Созданные файлы:

1. **`app.py`** — основное Flask-приложение с API endpoints
2. **`image_generator_utils.py`** — модуль с функциями генерации (переиспользует логику из CLI)
3. **`templates/index.html`** — HTML-шаблон с формой и интерфейсом
4. **`static/css/style.css`** — стили с градиентами и анимациями
5. **`static/js/main.js`** — JavaScript для AJAX-запросов и прогресс-бара

## Реализованные функции:

1. Поле для промпта — текстовое поле для описания изображения
2. Выбор стиля — 10 предустановленных стилей:
   - Реалистичный
   - Аниме
   - Киберпанк
   - Фэнтези
   - Акварель
   - Масляная живопись
   - Эскиз
   - 3D рендер
   - Винтаж
   - Минимализм
3. Улучшение промпта через GigaChat — опциональная галочка
4. Прогресс-бар — отображает статус генерации в реальном времени
5. Возможность новых запросов — кнопка для создания нового запроса

## Как запустить:

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Установите переменные окружения:
   ```powershell
   $env:GIGACHAT_CLIENT_ID="your-client-id"
   $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
   $env:OPENAI_KEY="your-openai-key"
   ```

3. Запустите приложение:
   ```bash
   python app.py
   ```

4. Откройте браузер: `http://localhost:5000`

Веб-интерфейс готов к использованию.

```shellscript
   pip install -r requirements.txt
```

```powershell
   $env:GIGACHAT_CLIENT_ID="your-client-id"
   $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
   $env:OPENAI_KEY="your-openai-key"
```

```shellscript
   python app.py
```

---

**User**

Сделай двойную генерацию, то есть:

Одновременно уходит запрос через penai напрямую и через proxyapi



нужно чтобы выводились оба варианта на экран и выводилось время генерации

---

**Cursor**


Изучаю текущий код для добавления параллельной генерации через OpenAI и ProxyAPI:



Добавляю параллельную генерацию через OpenAI и ProxyAPI. Обновляю код:


```python
"""
Утилиты для генерации изображений
"""

import os
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# Предопределенные стили промптов
STYLE_PROMPTS = {
    "realistic": "photorealistic, highly detailed, professional photography, sharp focus, 8k resolution",
    "anime": "anime style, vibrant colors, detailed character design, Japanese animation style, high quality",
    "cyberpunk": "cyberpunk aesthetic, neon lights, futuristic cityscape, dark atmosphere, sci-fi elements",
    "fantasy": "fantasy art style, magical atmosphere, epic composition, detailed fantasy elements, mystical lighting",
    "watercolor": "watercolor painting style, soft colors, artistic brushstrokes, dreamy atmosphere, artistic",
    "oil_painting": "oil painting style, classical art, rich colors, detailed brushwork, museum quality",
    "sketch": "pencil sketch style, black and white, detailed linework, artistic drawing, monochrome",
    "3d_render": "3D render, CGI, computer graphics, highly detailed, professional 3D modeling, realistic lighting",
    "vintage": "vintage style, retro aesthetic, aged look, classic photography, nostalgic atmosphere",
    "minimalist": "minimalist style, clean composition, simple design, modern aesthetic, elegant simplicity"
}


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    auth_key = os.getenv("GIGACHAT_CLIENT_SECRET")
    if not auth_key:
        raise ValueError("Переменная окружения GIGACHAT_CLIENT_SECRET не установлена")
    return auth_key


def get_gigachat_rquid():
    """Получает RqUID для запроса к GigaChat API"""
    rquid = os.getenv("GIGACHAT_CLIENT_ID")
    if not rquid:
        rquid = str(uuid.uuid4())  # Используем UUID если не задан
    return rquid


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    rquid = get_gigachat_rquid()

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rquid,
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        raise Exception(f"Ошибка при получении токена доступа GigaChat: {str(e)}")


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        raise ValueError("Переменная окружения OPENAI_KEY не установлена")
    return api_key


def get_proxy_api_key():
    """Получает ключ ProxyAPI из переменной окружения"""
    api_key = os.getenv("PROXY_API")
    if not api_key:
        raise ValueError("Переменная окружения PROXY_API не установлена")
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API через HTTP запросы"""
    try:
        access_token = get_gigachat_access_token()
        
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            'model': 'GigaChat',
            'messages': [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        }
        
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        response_data = response.json()
        choices = response_data.get('choices', [])
        if choices:
            refined_prompt = choices[0].get('message', {}).get('content', '').strip()
        else:
            raise ValueError("Пустой ответ от GigaChat API")
        
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        return refined_prompt
        
    except Exception as e:
        raise Exception(f"Ошибка при улучшении промпта через GigaChat: {str(e)}")


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image(prompt, style=None):
    """Генерирует изображение по промпту и сохраняет его"""
    try:
        # Добавляем стиль к промпту если указан
        if style and style in STYLE_PROMPTS:
            prompt = f"{prompt}, {STYLE_PROMPTS[style]}"
        
        api_key = get_openai_key()
        client = OpenAI(api_key=api_key)
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Скачивание изображения
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла
        output_dir = create_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        return {
            'filepath': str(filepath),
            'filename': filename,
            'url': image_url,
            'prompt': prompt
        }
        
    except Exception as e:
        raise Exception(f"Ошибка при генерации изображения: {str(e)}")


```

```python
"""
Утилиты для генерации изображений
"""

import os
import uuid
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# Предопределенные стили промптов
STYLE_PROMPTS = {
    "realistic": "photorealistic, highly detailed, professional photography, sharp focus, 8k resolution",
    "anime": "anime style, vibrant colors, detailed character design, Japanese animation style, high quality",
    "cyberpunk": "cyberpunk aesthetic, neon lights, futuristic cityscape, dark atmosphere, sci-fi elements",
    "fantasy": "fantasy art style, magical atmosphere, epic composition, detailed fantasy elements, mystical lighting",
    "watercolor": "watercolor painting style, soft colors, artistic brushstrokes, dreamy atmosphere, artistic",
    "oil_painting": "oil painting style, classical art, rich colors, detailed brushwork, museum quality",
    "sketch": "pencil sketch style, black and white, detailed linework, artistic drawing, monochrome",
    "3d_render": "3D render, CGI, computer graphics, highly detailed, professional 3D modeling, realistic lighting",
    "vintage": "vintage style, retro aesthetic, aged look, classic photography, nostalgic atmosphere",
    "minimalist": "minimalist style, clean composition, simple design, modern aesthetic, elegant simplicity"
}


def get_gigachat_auth_key():
    """Получает ключ авторизации GigaChat из переменной окружения"""
    auth_key = os.getenv("GIGACHAT_CLIENT_SECRET")
    if not auth_key:
        raise ValueError("Переменная окружения GIGACHAT_CLIENT_SECRET не установлена")
    return auth_key


def get_gigachat_rquid():
    """Получает RqUID для запроса к GigaChat API"""
    rquid = os.getenv("GIGACHAT_CLIENT_ID")
    if not rquid:
        rquid = str(uuid.uuid4())  # Используем UUID если не задан
    return rquid


def get_gigachat_access_token():
    """Получает токен доступа GigaChat через OAuth"""
    auth_key = get_gigachat_auth_key()
    rquid = get_gigachat_rquid()

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rquid,
        'Authorization': f'Basic {auth_key}'
    }
    data = {'scope': 'GIGACHAT_API_PERS'}
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        token_data = response.json()
        return token_data.get('access_token')
    except Exception as e:
        raise Exception(f"Ошибка при получении токена доступа GigaChat: {str(e)}")


def get_openai_key():
    """Получает ключ OpenAI из переменной окружения"""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        raise ValueError("Переменная окружения OPENAI_KEY не установлена")
    return api_key


def get_proxy_api_key():
    """Получает ключ ProxyAPI из переменной окружения"""
    api_key = os.getenv("PROXY_API")
    if not api_key:
        raise ValueError("Переменная окружения PROXY_API не установлена")
    return api_key


def refine_prompt_with_gigachat(prompt):
    """Улучшает промпт с помощью GigaChat API через HTTP запросы"""
    try:
        access_token = get_gigachat_access_token()
        
        system_message = (
            "Ты - эксперт по созданию детальных и конкретных промптов для генерации изображений. "
            "Твоя задача - улучшить пользовательский промпт, добавив конкретные детали о стиле, "
            "композиции, освещении, цветовой палитре и других важных аспектах изображения. "
            "Ответь ТОЛЬКО улучшенным промптом на английском языке, без дополнительных объяснений."
        )
        
        user_message = f"Улучши следующий промпт для генерации изображения, сделай его более детальным и конкретным: {prompt}"
        
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            'model': 'GigaChat',
            'messages': [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        }
        
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        response_data = response.json()
        choices = response_data.get('choices', [])
        if choices:
            refined_prompt = choices[0].get('message', {}).get('content', '').strip()
        else:
            raise ValueError("Пустой ответ от GigaChat API")
        
        refined_prompt = refined_prompt.strip('"').strip("'").strip()
        return refined_prompt
        
    except Exception as e:
        raise Exception(f"Ошибка при улучшении промпта через GigaChat: {str(e)}")


def create_output_directory():
    """Создает директорию для сохранения изображений"""
    output_dir = Path("generated_images")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def generate_image_openai(prompt, style=None):
    """Генерирует изображение через OpenAI DALL-E 3"""
    try:
        # Добавляем стиль к промпту если указан
        if style and style in STYLE_PROMPTS:
            prompt = f"{prompt}, {STYLE_PROMPTS[style]}"
        
        api_key = get_openai_key()
        client = OpenAI(api_key=api_key)
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Скачивание изображения
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Создание имени файла
        output_dir = create_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_openai.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_response.content)
        
        return {
            'filepath': str(filepath),
            'filename': filename,
            'url': image_url,
            'prompt': prompt,
            'source': 'OpenAI'
        }
        
    except Exception as e:
        raise Exception(f"Ошибка при генерации изображения через OpenAI: {str(e)}")


def generate_image_proxyapi(prompt, style=None):
    """Генерирует изображение через ProxyAPI GPT-Image"""
    import base64
    
    try:
        # Добавляем стиль к промпту если указан
        if style and style in STYLE_PROMPTS:
            prompt = f"{prompt}, {STYLE_PROMPTS[style]}"
        
        api_key = get_proxy_api_key()
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.proxyapi.ru/openai/v1",
        )
        
        # Генерация изображения через ProxyAPI
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt
        )
        
        # Получение base64 изображения
        image_base64 = result.data[0].b64_json
        
        # Декодирование base64 в байты
        image_bytes = base64.b64decode(image_base64)
        
        # Создание имени файла
        output_dir = create_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        filename = f"{timestamp}_{safe_prompt}_proxyapi.png"
        filepath = output_dir / filename
        
        # Сохранение изображения
        with open(filepath, 'wb') as f:
            f.write(image_bytes)
        
        return {
            'filepath': str(filepath),
            'filename': filename,
            'url': None,  # ProxyAPI возвращает base64, не URL
            'prompt': prompt,
            'source': 'ProxyAPI'
        }
        
    except Exception as e:
        raise Exception(f"Ошибка при генерации изображения через ProxyAPI: {str(e)}")


# Обратная совместимость
def generate_image(prompt, style=None):
    """Генерирует изображение по промпту (для обратной совместимости)"""
    return generate_image_openai(prompt, style)


```

```python
"""
Flask веб-приложение для генерации изображений
"""

import os
import threading
import time
from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path
from image_generator_utils import (
    refine_prompt_with_gigachat,
    generate_image_openai,
    generate_image_proxyapi,
    STYLE_PROMPTS
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Хранилище статусов задач
tasks_status = {}


def generate_single_image(api_type, prompt, style, task_id, result_key):
    """Генерирует одно изображение через указанный API"""
    start_time = time.time()
    try:
        if api_type == 'openai':
            result = generate_image_openai(prompt, style)
        elif api_type == 'proxyapi':
            result = generate_image_proxyapi(prompt, style)
        else:
            raise ValueError(f"Неизвестный тип API: {api_type}")
        
        elapsed_time = time.time() - start_time
        result['generation_time'] = round(elapsed_time, 2)
        
        tasks_status[task_id][result_key] = {
            'status': 'completed',
            'result': result
        }
        
    except Exception as e:
        elapsed_time = time.time() - start_time
        tasks_status[task_id][result_key] = {
            'status': 'error',
            'error': str(e),
            'generation_time': round(elapsed_time, 2)
        }


def process_generation_task(task_id, prompt, style, use_gigachat):
    """Обрабатывает задачу генерации изображения в отдельном потоке"""
    try:
        tasks_status[task_id] = {
            'status': 'processing',
            'progress': 10,
            'message': 'Начало обработки...',
            'openai': {'status': 'pending'},
            'proxyapi': {'status': 'pending'}
        }
        
        final_prompt = prompt
        
        # Улучшение промпта через GigaChat
        if use_gigachat:
            tasks_status[task_id]['progress'] = 20
            tasks_status[task_id]['message'] = 'Улучшение промпта через GigaChat...'
            try:
                refined = refine_prompt_with_gigachat(prompt)
                final_prompt = refined
                tasks_status[task_id]['progress'] = 30
                tasks_status[task_id]['message'] = 'Промпт улучшен, запуск параллельной генерации...'
            except Exception as e:
                tasks_status[task_id]['progress'] = 25
                tasks_status[task_id]['message'] = f'Ошибка улучшения промпта: {str(e)}, используем исходный промпт'
        else:
            tasks_status[task_id]['progress'] = 30
            tasks_status[task_id]['message'] = 'Запуск параллельной генерации...'
        
        # Запускаем параллельную генерацию через оба API
        tasks_status[task_id]['progress'] = 40
        tasks_status[task_id]['message'] = 'Генерация через OpenAI и ProxyAPI...'
        
        # Создаем потоки для параллельной генерации
        thread_openai = threading.Thread(
            target=generate_single_image,
            args=('openai', final_prompt, style, task_id, 'openai')
        )
        thread_proxyapi = threading.Thread(
            target=generate_single_image,
            args=('proxyapi', final_prompt, style, task_id, 'proxyapi')
        )
        
        thread_openai.daemon = True
        thread_proxyapi.daemon = True
        
        thread_openai.start()
        thread_proxyapi.start()
        
        # Ждем завершения обоих потоков
        thread_openai.join()
        thread_proxyapi.join()
        
        # Проверяем результаты
        openai_result = tasks_status[task_id]['openai']
        proxyapi_result = tasks_status[task_id]['proxyapi']
        
        # Определяем общий статус
        if openai_result['status'] == 'completed' or proxyapi_result['status'] == 'completed':
            tasks_status[task_id]['status'] = 'completed'
            tasks_status[task_id]['progress'] = 100
            tasks_status[task_id]['message'] = 'Готово!'
        else:
            tasks_status[task_id]['status'] = 'error'
            tasks_status[task_id]['progress'] = 0
            errors = []
            if openai_result['status'] == 'error':
                errors.append(f"OpenAI: {openai_result.get('error', 'Неизвестная ошибка')}")
            if proxyapi_result['status'] == 'error':
                errors.append(f"ProxyAPI: {proxyapi_result.get('error', 'Неизвестная ошибка')}")
            tasks_status[task_id]['message'] = 'Ошибки: ' + '; '.join(errors)
        
    except Exception as e:
        tasks_status[task_id] = {
            'status': 'error',
            'progress': 0,
            'message': f'Ошибка: {str(e)}',
            'openai': {'status': 'error', 'error': str(e)},
            'proxyapi': {'status': 'error', 'error': str(e)}
        }


@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', styles=STYLE_PROMPTS.keys())


@app.route('/api/generate', methods=['POST'])
def api_generate():
    """API endpoint для запуска генерации изображения"""
    data = request.json
    prompt = data.get('prompt', '').strip()
    style = data.get('style', '')
    use_gigachat = data.get('use_gigachat', False)
    
    if not prompt:
        return jsonify({'error': 'Промпт не может быть пустым'}), 400
    
    # Создаем уникальный ID задачи
    task_id = f"task_{int(time.time() * 1000)}"
    
    # Инициализируем статус задачи
    tasks_status[task_id] = {'status': 'queued', 'progress': 0, 'message': 'Задача поставлена в очередь...'}
    
    # Запускаем генерацию в отдельном потоке
    thread = threading.Thread(
        target=process_generation_task,
        args=(task_id, prompt, style, use_gigachat)
    )
    thread.daemon = True
    thread.start()
    
    return jsonify({'task_id': task_id})


@app.route('/api/status/<task_id>')
def api_status(task_id):
    """API endpoint для проверки статуса задачи"""
    if task_id not in tasks_status:
        return jsonify({'error': 'Задача не найдена'}), 404
    
    return jsonify(tasks_status[task_id])


@app.route('/generated_images/<filename>')
def serve_image(filename):
    """Отдает сгенерированные изображения"""
    return send_from_directory('generated_images', filename)


@app.route('/api/styles')
def api_styles():
    """API endpoint для получения списка стилей"""
    return jsonify({'styles': list(STYLE_PROMPTS.keys())})


if __name__ == '__main__':
    # Создаем директорию для изображений если её нет
    Path('generated_images').mkdir(exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)


```


Обновляю HTML и JavaScript для отображения двух изображений и времени генерации:


```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Генератор изображений</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <header>
            <h1>🎨 Генератор изображений</h1>
            <p class="subtitle">Создавайте уникальные изображения с помощью AI</p>
        </header>

        <main>
            <div class="form-container">
                <form id="generateForm">
                    <div class="form-group">
                        <label for="prompt">Описание изображения:</label>
                        <textarea 
                            id="prompt" 
                            name="prompt" 
                            rows="4" 
                            placeholder="Введите описание того, что вы хотите увидеть на изображении..."
                            required
                        ></textarea>
                    </div>

                    <div class="form-group">
                        <label for="style">Стиль изображения:</label>
                        <select id="style" name="style">
                            <option value="">Без стиля</option>
                            <option value="realistic">Реалистичный</option>
                            <option value="anime">Аниме</option>
                            <option value="cyberpunk">Киберпанк</option>
                            <option value="fantasy">Фэнтези</option>
                            <option value="watercolor">Акварель</option>
                            <option value="oil_painting">Масляная живопись</option>
                            <option value="sketch">Эскиз</option>
                            <option value="3d_render">3D рендер</option>
                            <option value="vintage">Винтаж</option>
                            <option value="minimalist">Минимализм</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label class="checkbox-label">
                            <input type="checkbox" id="use_gigachat" name="use_gigachat" checked>
                            <span>Улучшить промпт через GigaChat</span>
                        </label>
                    </div>

                    <button type="submit" id="generateBtn" class="btn-primary">
                        Сгенерировать изображение
                    </button>
                </form>
            </div>

            <!-- Прогресс бар -->
            <div id="progressContainer" class="progress-container" style="display: none;">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar">
                        <div id="progressBar" class="progress-bar-fill"></div>
                    </div>
                    <div id="progressText" class="progress-text">0%</div>
                </div>
                <div id="progressMessage" class="progress-message"></div>
            </div>

            <!-- Результат -->
            <div id="resultContainer" class="result-container" style="display: none;">
                <h2>Результаты генерации:</h2>
                <div id="resultContent" class="result-content">
                    <!-- Здесь будут отображаться изображения -->
                </div>
                <div class="result-actions">
                    <button id="newRequestBtn" class="btn-secondary">Создать новый запрос</button>
                </div>
            </div>

            <!-- Ошибка -->
            <div id="errorContainer" class="error-container" style="display: none;">
                <div class="error-message">
                    <span id="errorText"></span>
                </div>
                <button id="closeErrorBtn" class="btn-secondary">Закрыть</button>
            </div>
        </main>
    </div>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>


```


Обновляю JavaScript для отображения двух изображений и времени генерации:


```javascript
// Обработка формы генерации
document.getElementById('generateForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const prompt = document.getElementById('prompt').value.trim();
    const style = document.getElementById('style').value;
    const useGigachat = document.getElementById('use_gigachat').checked;
    
    if (!prompt) {
        showError('Пожалуйста, введите описание изображения');
        return;
    }
    
    // Скрываем предыдущие результаты и ошибки
    hideResult();
    hideError();
    
    // Показываем прогресс бар
    showProgress();
    
    // Отправляем запрос на генерацию
    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt: prompt,
                style: style,
                use_gigachat: useGigachat
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Ошибка при отправке запроса');
        }
        
        const data = await response.json();
        const taskId = data.task_id;
        
        // Начинаем отслеживание статуса
        pollStatus(taskId);
        
    } catch (error) {
        hideProgress();
        showError(error.message);
    }
});

// Функция для опроса статуса задачи
async function pollStatus(taskId) {
    const maxAttempts = 300; // Максимум 5 минут (300 * 1 секунда)
    let attempts = 0;
    
    const interval = setInterval(async () => {
        attempts++;
        
        try {
            const response = await fetch(`/api/status/${taskId}`);
            
            if (!response.ok) {
                throw new Error('Ошибка при проверке статуса');
            }
            
            const status = await response.json();
            
            // Обновляем прогресс бар
            updateProgress(status.progress, status.message);
            
            // Обновляем статусы отдельных API
            updateApiStatus(status);
            
            if (status.status === 'completed') {
                clearInterval(interval);
                hideProgress();
                showResult(status);
            } else if (status.status === 'error') {
                clearInterval(interval);
                hideProgress();
                showError(status.message);
            } else if (attempts >= maxAttempts) {
                clearInterval(interval);
                hideProgress();
                showError('Превышено время ожидания. Попробуйте еще раз.');
            }
            
        } catch (error) {
            clearInterval(interval);
            hideProgress();
            showError(error.message);
        }
    }, 1000); // Проверяем каждую секунду
}

// Обновление статусов отдельных API
function updateApiStatus(status) {
    // Можно добавить визуализацию статуса каждого API в прогресс-баре
    // Пока просто обновляем общий прогресс
}

// Функции для управления UI
function showProgress() {
    document.getElementById('progressContainer').style.display = 'block';
    document.getElementById('generateBtn').disabled = true;
    updateProgress(0, 'Инициализация...');
}

function hideProgress() {
    document.getElementById('progressContainer').style.display = 'none';
    document.getElementById('generateBtn').disabled = false;
}

function updateProgress(percent, message) {
    document.getElementById('progressBar').style.width = percent + '%';
    document.getElementById('progressText').textContent = percent + '%';
    document.getElementById('progressMessage').textContent = message;
}

function showResult(result) {
    const container = document.getElementById('resultContainer');
    const content = document.getElementById('resultContent');
    
    content.innerHTML = `
        <img src="/generated_images/${result.filename}" alt="Generated image">
        <div class="result-info">
            <p><strong>Промпт:</strong> ${escapeHtml(result.prompt)}</p>
            <p><strong>Файл:</strong> ${result.filename}</p>
        </div>
    `;
    
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideResult() {
    document.getElementById('resultContainer').style.display = 'none';
}

function showError(message) {
    const container = document.getElementById('errorContainer');
    const errorText = document.getElementById('errorText');
    
    errorText.textContent = message;
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
    document.getElementById('errorContainer').style.display = 'none';
}

// Обработчик кнопки "Создать новый запрос"
document.getElementById('newRequestBtn').addEventListener('click', () => {
    hideResult();
    hideError();
    document.getElementById('prompt').value = '';
    document.getElementById('style').value = '';
    document.getElementById('prompt').focus();
});

// Обработчик кнопки закрытия ошибки
document.getElementById('closeErrorBtn').addEventListener('click', () => {
    hideError();
});

// Функция для экранирования HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}


```

```javascript
// Обработка формы генерации
document.getElementById('generateForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const prompt = document.getElementById('prompt').value.trim();
    const style = document.getElementById('style').value;
    const useGigachat = document.getElementById('use_gigachat').checked;
    
    if (!prompt) {
        showError('Пожалуйста, введите описание изображения');
        return;
    }
    
    // Скрываем предыдущие результаты и ошибки
    hideResult();
    hideError();
    
    // Показываем прогресс бар
    showProgress();
    
    // Отправляем запрос на генерацию
    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt: prompt,
                style: style,
                use_gigachat: useGigachat
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Ошибка при отправке запроса');
        }
        
        const data = await response.json();
        const taskId = data.task_id;
        
        // Начинаем отслеживание статуса
        pollStatus(taskId);
        
    } catch (error) {
        hideProgress();
        showError(error.message);
    }
});

// Функция для опроса статуса задачи
async function pollStatus(taskId) {
    const maxAttempts = 300; // Максимум 5 минут (300 * 1 секунда)
    let attempts = 0;
    
    const interval = setInterval(async () => {
        attempts++;
        
        try {
            const response = await fetch(`/api/status/${taskId}`);
            
            if (!response.ok) {
                throw new Error('Ошибка при проверке статуса');
            }
            
            const status = await response.json();
            
            // Обновляем прогресс бар
            updateProgress(status.progress, status.message);
            
            // Обновляем статусы отдельных API
            updateApiStatus(status);
            
            if (status.status === 'completed') {
                clearInterval(interval);
                hideProgress();
                showResult(status);
            } else if (status.status === 'error') {
                clearInterval(interval);
                hideProgress();
                showError(status.message);
            } else if (attempts >= maxAttempts) {
                clearInterval(interval);
                hideProgress();
                showError('Превышено время ожидания. Попробуйте еще раз.');
            }
            
        } catch (error) {
            clearInterval(interval);
            hideProgress();
            showError(error.message);
        }
    }, 1000); // Проверяем каждую секунду
}

// Обновление статусов отдельных API
function updateApiStatus(status) {
    // Можно добавить визуализацию статуса каждого API в прогресс-баре
    // Пока просто обновляем общий прогресс
}

// Функции для управления UI
function showProgress() {
    document.getElementById('progressContainer').style.display = 'block';
    document.getElementById('generateBtn').disabled = true;
    updateProgress(0, 'Инициализация...');
}

function hideProgress() {
    document.getElementById('progressContainer').style.display = 'none';
    document.getElementById('generateBtn').disabled = false;
}

function updateProgress(percent, message) {
    document.getElementById('progressBar').style.width = percent + '%';
    document.getElementById('progressText').textContent = percent + '%';
    document.getElementById('progressMessage').textContent = message;
}

function showResult(status) {
    const container = document.getElementById('resultContainer');
    const content = document.getElementById('resultContent');
    
    let html = '<div class="results-grid">';
    
    // OpenAI результат
    const openaiResult = status.openai;
    if (openaiResult && openaiResult.status === 'completed' && openaiResult.result) {
        const result = openaiResult.result;
        html += `
            <div class="result-item">
                <h3>OpenAI DALL-E 3</h3>
                <img src="/generated_images/${result.filename}" alt="OpenAI generated image">
                <div class="result-info">
                    <p><strong>Время генерации:</strong> ${result.generation_time} сек</p>
                    <p><strong>Промпт:</strong> ${escapeHtml(result.prompt)}</p>
                    <p><strong>Файл:</strong> ${result.filename}</p>
                </div>
            </div>
        `;
    } else if (openaiResult && openaiResult.status === 'error') {
        html += `
            <div class="result-item error-item">
                <h3>OpenAI DALL-E 3</h3>
                <div class="error-message-small">
                    Ошибка: ${escapeHtml(openaiResult.error || 'Неизвестная ошибка')}
                </div>
                ${openaiResult.generation_time ? `<p><strong>Время до ошибки:</strong> ${openaiResult.generation_time} сек</p>` : ''}
            </div>
        `;
    } else {
        html += `
            <div class="result-item pending-item">
                <h3>OpenAI DALL-E 3</h3>
                <div class="pending-message">Ожидание результата...</div>
            </div>
        `;
    }
    
    // ProxyAPI результат
    const proxyapiResult = status.proxyapi;
    if (proxyapiResult && proxyapiResult.status === 'completed' && proxyapiResult.result) {
        const result = proxyapiResult.result;
        html += `
            <div class="result-item">
                <h3>ProxyAPI GPT-Image</h3>
                <img src="/generated_images/${result.filename}" alt="ProxyAPI generated image">
                <div class="result-info">
                    <p><strong>Время генерации:</strong> ${result.generation_time} сек</p>
                    <p><strong>Промпт:</strong> ${escapeHtml(result.prompt)}</p>
                    <p><strong>Файл:</strong> ${result.filename}</p>
                </div>
            </div>
        `;
    } else if (proxyapiResult && proxyapiResult.status === 'error') {
        html += `
            <div class="result-item error-item">
                <h3>ProxyAPI GPT-Image</h3>
                <div class="error-message-small">
                    Ошибка: ${escapeHtml(proxyapiResult.error || 'Неизвестная ошибка')}
                </div>
                ${proxyapiResult.generation_time ? `<p><strong>Время до ошибки:</strong> ${proxyapiResult.generation_time} сек</p>` : ''}
            </div>
        `;
    } else {
        html += `
            <div class="result-item pending-item">
                <h3>ProxyAPI GPT-Image</h3>
                <div class="pending-message">Ожидание результата...</div>
            </div>
        `;
    }
    
    html += '</div>';
    
    content.innerHTML = html;
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideResult() {
    document.getElementById('resultContainer').style.display = 'none';
}

function showError(message) {
    const container = document.getElementById('errorContainer');
    const errorText = document.getElementById('errorText');
    
    errorText.textContent = message;
    container.style.display = 'block';
    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
    document.getElementById('errorContainer').style.display = 'none';
}

// Обработчик кнопки "Создать новый запрос"
document.getElementById('newRequestBtn').addEventListener('click', () => {
    hideResult();
    hideError();
    document.getElementById('prompt').value = '';
    document.getElementById('style').value = '';
    document.getElementById('prompt').focus();
});

// Обработчик кнопки закрытия ошибки
document.getElementById('closeErrorBtn').addEventListener('click', () => {
    hideError();
});

// Функция для экранирования HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}


```


Добавляю CSS-стили для отображения двух изображений:


```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    overflow: hidden;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px 30px;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    font-weight: 700;
}

.subtitle {
    font-size: 1.1em;
    opacity: 0.9;
}

main {
    padding: 40px 30px;
}

.form-container {
    margin-bottom: 30px;
}

.form-group {
    margin-bottom: 25px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #555;
    font-size: 1em;
}

textarea,
select {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1em;
    font-family: inherit;
    transition: border-color 0.3s;
}

textarea:focus,
select:focus {
    outline: none;
    border-color: #667eea;
}

textarea {
    resize: vertical;
    min-height: 100px;
}

.checkbox-label {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-weight: normal;
}

.checkbox-label input[type="checkbox"] {
    width: auto;
    margin-right: 10px;
    cursor: pointer;
    transform: scale(1.2);
}

.btn-primary,
.btn-secondary {
    padding: 15px 30px;
    border: none;
    border-radius: 10px;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    width: 100%;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-primary:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
}

.btn-primary:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.btn-secondary {
    background: #f0f0f0;
    color: #333;
    margin-top: 15px;
}

.btn-secondary:hover {
    background: #e0e0e0;
}

/* Прогресс бар */
.progress-container {
    margin: 30px 0;
    padding: 25px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.progress-bar-wrapper {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.progress-bar {
    flex: 1;
    height: 30px;
    background: #e0e0e0;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
}

.progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    transition: width 0.3s ease;
    width: 0%;
    position: relative;
    overflow: hidden;
}

.progress-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.3),
        transparent
    );
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(100%);
    }
}

.progress-text {
    font-weight: 600;
    font-size: 1.1em;
    color: #667eea;
    min-width: 50px;
    text-align: right;
}

.progress-message {
    color: #666;
    font-size: 0.95em;
    text-align: center;
}

/* Результат */
.result-container {
    margin: 30px 0;
    padding: 30px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.result-container h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 1.8em;
}

.result-content {
    text-align: center;
}

.results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
    margin-bottom: 20px;
}

.result-item {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    border: 2px solid #e0e0e0;
}

.result-item h3 {
    margin-bottom: 15px;
    color: #667eea;
    font-size: 1.3em;
    text-align: center;
}

.result-item img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    margin-bottom: 15px;
}

.result-item.error-item {
    border-color: #fc8181;
    background: #fff5f5;
}

.result-item.pending-item {
    border-color: #fbbf24;
    background: #fffbeb;
}

.error-message-small {
    color: #c53030;
    font-weight: 600;
    padding: 15px;
    background: white;
    border-radius: 10px;
    margin-bottom: 10px;
}

.pending-message {
    color: #92400e;
    font-weight: 600;
    padding: 15px;
    text-align: center;
    font-size: 1.1em;
}

.result-info {
    margin-top: 20px;
    padding: 15px;
    background: white;
    border-radius: 10px;
    text-align: left;
}

.result-info p {
    margin: 10px 0;
    color: #666;
}

.result-info strong {
    color: #333;
}

.result-actions {
    margin-top: 20px;
}

/* Ошибка */
.error-container {
    margin: 30px 0;
    padding: 25px;
    background: #fff5f5;
    border: 2px solid #fc8181;
    border-radius: 15px;
}

.error-message {
    color: #c53030;
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 1.1em;
}

/* Анимации */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.result-container,
.progress-container,
.error-container {
    animation: fadeIn 0.5s ease;
}

/* Адаптивность */
@media (max-width: 768px) {
    header h1 {
        font-size: 2em;
    }

    main {
        padding: 20px;
    }

    .progress-bar-wrapper {
        flex-direction: column;
        gap: 10px;
    }

    .progress-text {
        text-align: center;
    }
}


```

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    overflow: hidden;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px 30px;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    font-weight: 700;
}

.subtitle {
    font-size: 1.1em;
    opacity: 0.9;
}

main {
    padding: 40px 30px;
}

.form-container {
    margin-bottom: 30px;
}

.form-group {
    margin-bottom: 25px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #555;
    font-size: 1em;
}

textarea,
select {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1em;
    font-family: inherit;
    transition: border-color 0.3s;
}

textarea:focus,
select:focus {
    outline: none;
    border-color: #667eea;
}

textarea {
    resize: vertical;
    min-height: 100px;
}

.checkbox-label {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-weight: normal;
}

.checkbox-label input[type="checkbox"] {
    width: auto;
    margin-right: 10px;
    cursor: pointer;
    transform: scale(1.2);
}

.btn-primary,
.btn-secondary {
    padding: 15px 30px;
    border: none;
    border-radius: 10px;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    width: 100%;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-primary:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
}

.btn-primary:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.btn-secondary {
    background: #f0f0f0;
    color: #333;
    margin-top: 15px;
}

.btn-secondary:hover {
    background: #e0e0e0;
}

/* Прогресс бар */
.progress-container {
    margin: 30px 0;
    padding: 25px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.progress-bar-wrapper {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.progress-bar {
    flex: 1;
    height: 30px;
    background: #e0e0e0;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
}

.progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    transition: width 0.3s ease;
    width: 0%;
    position: relative;
    overflow: hidden;
}

.progress-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.3),
        transparent
    );
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(100%);
    }
}

.progress-text {
    font-weight: 600;
    font-size: 1.1em;
    color: #667eea;
    min-width: 50px;
    text-align: right;
}

.progress-message {
    color: #666;
    font-size: 0.95em;
    text-align: center;
}

/* Результат */
.result-container {
    margin: 30px 0;
    padding: 30px;
    background: #f8f9fa;
    border-radius: 15px;
    border: 2px solid #e0e0e0;
}

.result-container h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 1.8em;
}

.result-content {
    text-align: center;
}

.results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
    margin-bottom: 20px;
}

.result-item {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    border: 2px solid #e0e0e0;
}

.result-item h3 {
    margin-bottom: 15px;
    color: #667eea;
    font-size: 1.3em;
    text-align: center;
}

.result-item img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    margin-bottom: 15px;
}

.result-item.error-item {
    border-color: #fc8181;
    background: #fff5f5;
}

.result-item.pending-item {
    border-color: #fbbf24;
    background: #fffbeb;
}

.error-message-small {
    color: #c53030;
    font-weight: 600;
    padding: 15px;
    background: white;
    border-radius: 10px;
    margin-bottom: 10px;
}

.pending-message {
    color: #92400e;
    font-weight: 600;
    padding: 15px;
    text-align: center;
    font-size: 1.1em;
}

.result-info {
    margin-top: 20px;
    padding: 15px;
    background: white;
    border-radius: 10px;
    text-align: left;
}

.result-info p {
    margin: 10px 0;
    color: #666;
}

.result-info strong {
    color: #333;
}

.result-actions {
    margin-top: 20px;
}

/* Ошибка */
.error-container {
    margin: 30px 0;
    padding: 25px;
    background: #fff5f5;
    border: 2px solid #fc8181;
    border-radius: 15px;
}

.error-message {
    color: #c53030;
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 1.1em;
}

/* Анимации */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.result-container,
.progress-container,
.error-container {
    animation: fadeIn 0.5s ease;
}

/* Адаптивность */
@media (max-width: 768px) {
    header h1 {
        font-size: 2em;
    }

    main {
        padding: 20px;
    }

    .progress-bar-wrapper {
        flex-direction: column;
        gap: 10px;
    }

    .progress-text {
        text-align: center;
    }

    .results-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}


```


Обновляю README с информацией о двойной генерации:


```markdown
# Генератор изображений

Приложения для генерации изображений:

**CLI приложения:**
- **image_generator.py** - использует OpenAI DALL-E 3
- **image_generator_proxy.py** - использует ProxyAPI GPT-Image 1
- **image_generator_gigachat.py** - улучшает промпт через GigaChat, затем генерирует через OpenAI DALL-E 3

**Веб-приложение:**
- **app.py** - Flask веб-интерфейс с выбором стилей, улучшением промпта через GigaChat и прогресс-баром

## Установка

1. Создайте виртуальное окружение:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите переменную окружения с ключом API:
   
   **Для OpenAI (image_generator.py):**
   - Windows (PowerShell):
     ```powershell
     $env:OPENAI_KEY="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set OPENAI_KEY=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export OPENAI_KEY=your-api-key-here
     ```
   
   **Для ProxyAPI (image_generator_proxy.py):**
   - Windows (PowerShell):
     ```powershell
     $env:PROXY_API="your-api-key-here"
     ```
   - Windows (CMD):
     ```cmd
     set PROXY_API=your-api-key-here
     ```
   - Linux/Mac:
     ```bash
     export PROXY_API=your-api-key-here
     ```
   
   **Для GigaChat + OpenAI (image_generator_gigachat.py и app.py):**
   - Windows (PowerShell):
     ```powershell
     $env:GIGACHAT_CLIENT_ID="your-client-id"
     $env:GIGACHAT_CLIENT_SECRET="your-client-secret"
     $env:OPENAI_KEY="your-openai-key"
     ```
   - Windows (CMD):
     ```cmd
     set GIGACHAT_CLIENT_ID=your-client-id
     set GIGACHAT_CLIENT_SECRET=your-client-secret
     set OPENAI_KEY=your-openai-key
     ```
   - Linux/Mac:
     ```bash
     export GIGACHAT_CLIENT_ID='your-client-id'
     export GIGACHAT_CLIENT_SECRET='your-client-secret'
     export OPENAI_KEY='your-openai-key'
     ```
   
   *Примечание: Для веб-приложения требуются все три переменные окружения*

## Использование

**OpenAI DALL-E 3:**
```bash
python image_generator.py
```

**ProxyAPI GPT-Image 1:**
```bash
python image_generator_proxy.py
```

**GigaChat + OpenAI (улучшение промпта):**
```bash
python image_generator_gigachat.py
```

**Веб-приложение Flask:**
```bash
python app.py
```

Затем откройте браузер и перейдите по адресу: `http://localhost:5000`

**Возможности веб-приложения:**
- Поле для ввода промпта
- Выбор стиля изображения (10 предустановленных стилей)
- Опция улучшения промпта через GigaChat
- **Двойная генерация**: одновременная генерация через OpenAI DALL-E 3 и ProxyAPI GPT-Image
- Отображение обоих результатов на экране
- Показ времени генерации для каждого API
- Прогресс-бар с отображением статуса генерации
- Просмотр результатов прямо в браузере
- Возможность создавать новые запросы

**Для веб-приложения также требуется:**
- Windows (PowerShell):
  ```powershell
  $env:PROXY_API="your-proxy-api-key"
  ```
- Windows (CMD):
  ```cmd
  set PROXY_API=your-proxy-api-key
  ```
- Linux/Mac:
  ```bash
  export PROXY_API='your-proxy-api-key'
  ```

**Примечание для image_generator_gigachat.py:** Скрипт сначала отправляет ваш промпт в GigaChat для улучшения и добавления конкретики, затем использует улучшенный промпт для генерации изображения через OpenAI DALL-E 3.

## Результаты

Все сгенерированные изображения сохраняются в директории `generated_images/` с временной меткой в имени файла.


```


Проверяю, что логика в `app.py` корректно обрабатывает параллельную генерацию:



Реализована двойная генерация. Итоги:

## Реализованные изменения:

1. **`image_generator_utils.py`**:
   - Добавлена функция `generate_image_proxyapi()` для генерации через ProxyAPI
   - Функция `generate_image_openai()` переименована из `generate_image()`
   - Добавлена функция `get_proxy_api_key()` для получения ключа ProxyAPI

2. **`app.py`**:
   - Обновлена функция `process_generation_task()` для параллельной генерации через оба API
   - Добавлена функция `generate_single_image()` для генерации одного изображения в отдельном потоке
   - Оба API запускаются параллельно в разных потоках
   - Отслеживается время генерации для каждого API

3. **`static/js/main.js`**:
   - Обновлена функция `showResult()` для отображения двух изображений
   - Добавлено отображение времени генерации для каждого API
   - Обработка ошибок для каждого API отдельно

4. **`static/css/style.css`**:
   - Добавлен grid layout для отображения двух результатов рядом
   - Стили для ошибок и ожидания результатов
   - Адаптивный дизайн для мобильных устройств

5. **`README.md`**:
   - Обновлена документация с информацией о двойной генерации

## Как это работает:

1. Пользователь вводит промпт и выбирает стиль
2. При необходимости промпт улучшается через GigaChat
3. Одновременно запускаются два потока:
   - OpenAI DALL-E 3
   - ProxyAPI GPT-Image
4. Оба результата отображаются на экране с временем генерации
5. Если один из API завершится с ошибкой, второй результат все равно отобразится

Веб-приложение готово к использованию с двойной генерацией.

