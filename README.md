# Items API

REST API для керування об'єктами (items), розроблений на Python із використанням FastAPI.

## Опис

Сервіс реалізує CRUD-операції для сутності Item. Дані зберігаються в пам'яті застосунку. Сервіс повертає відповіді у форматі JSON, використовує коректні HTTP status codes та підтримує специфікацію OpenAPI зі Swagger UI.

## Технології

- Python 3.12
- FastAPI
- Pytest
- Docker
- GitHub
- Azure DevOps
- Docker Hub

## Функціональність

| Метод | Endpoint | Опис |
|---|---|---|
| GET | /api/items | Отримати список об'єктів |
| GET | /api/items/{item_id} | Отримати об'єкт за ідентифікатором |
| POST | /api/items | Створити новий об'єкт |
| PUT | /api/items/{item_id} | Оновити наявний об'єкт |
| DELETE | /api/items/{item_id} | Видалити об'єкт |

## Документація API

Після запуску сервісу доступні:

- Swagger UI: http://localhost:8000/docs
- OpenAPI-специфікація: http://localhost:8000/openapi.json

## Локальний запуск

```bash
python -m venv .venv
.venv\Scripts\activate        
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Збирання та запуск Docker-образу

```bash
docker build -t items-api .
docker run -p 8000:8000 items-api
```

Після запуску Swagger UI доступний за адресою http://localhost:8000/docs

## Запуск тестів

```bash
pip install -r requirements.txt
pytest
```

## CI/CD

Azure DevOps pipeline автоматично запускається після push у гілку `main` і виконує: встановлення залежностей, запуск unit-тестів, збирання Docker-образу, присвоєння тегів та публікацію образу в Docker Hub.
