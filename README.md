# Task planner

## Описание:

Тестовое задание по созданию планировщика задач.

В качестве фрейворка использован FastAPI.

Для подключения базы данных используется SQLAlchemy 1.4

Структура приложения построена по функциональному признаку

Приложение позволяет:
* создать задачу
* изменить задачу
* удалить задачу
* получить список задач

## Технологии:

* Python 3.10
* FastAPI 0.78
* SQLAlchemy 1.4
* Alembic 1.7

## Установка и запуск:

* Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:MPolskov/task_planner.git
```

```
cd task_planner
```

* Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

* Обновить pip и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* В корневой директории создать файл .env с переменными окружения (пример содержания файла приведен в .env.example)

* Применить миграции:

```
alembic upgrade head
```

* Запустить приложение:

```
uvicorn app.main:app
```

### Документация OpenAPI доступна по ссылке: http://127.0.0.1:8000/docs

## Автор:

### Полшков Михаил
