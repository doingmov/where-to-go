# Куда пойти ?

Сайт-афиша необычных мест Москвы: антикафе, арт-пространства, смотровые площадки и другие интересные локации на интерактивной карте.

Учебный проект на платформе [Devman](https://dvmn.org/). Тестовые данные о локациях взяты с сайта [KudaGo](https://kudago.com).

## Как это выглядит

На главной странице — карта Москвы с метками интересных мест. Клик по метке открывает карточку с фотографиями, коротким и подробным описанием локации.

## Как установить

Проект на Python 3 и Django 5.2.

1. Склонируй репозиторий и перейди в папку проекта:
   ```bash
   git clone https://github.com/<твой-логин>/where-to-go.git
   cd where-to-go
   ```

2. Создай и активируй виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate.bat     # Windows
   ```

3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создай файл `.env` в корне проекта (рядом с `manage.py`):
   ```
   DJANGO_SECRET_KEY=сгенерируй-свой-секретный-ключ
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. Примени миграции и создай аккаунт администратора:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Как наполнить сайт данными

Тестовые локации хранятся в виде JSON-файлов в репозитории [where-to-go-places](https://github.com/devmanorg/where-to-go-places). Загрузить локацию на сайт можно командой:

```bash
python manage.py load_place <адрес JSON-файла>
```

Например:
```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json
```

Команда сама скачает текст, координаты и фотографии локации и сохранит их в базу данных.

## Как запустить

```bash
python manage.py runserver
```

- Сайт: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Админка: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Возможности админки

- Поиск и редактирование локаций по названию
- Загрузка и превью фотографий прямо на странице локации
- Сортировка фотографий перетаскиванием (drag-and-drop)
- WYSIWYG-редактор для подробного описания локации

## Технологии

- Python 3, Django 5.2
- [django-tinymce](https://github.com/aljosa/django-tinymce) — редактор текста в админке
- [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/) — сортировка фотографий
- [Leaflet](https://leafletjs.com/), [Vue.js](https://v2.vuejs.org/), Bootstrap — фронтенд карты (см. [where-to-go-frontend](https://github.com/devmanorg/where-to-go-frontend))

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
