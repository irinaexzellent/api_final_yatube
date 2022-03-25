# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:irinaexzellent/api_final_yatube.git
```

```
cd ytube_api
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```
```
source venc/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```

# Примеры запросов API:

**Получение публикаций. Создание публикаций**
```
/api/v1/posts/
```
*Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
Добавить новую публикацию в коллекцию публикаций. Доступно аутифицированным пользователям*

**Получение, обновление, частичное обновление, удаление публикации.**
```
/api/v1/posts/{id}/
```
*Обновить, частично обновить, удалить может только автор публикации. Доступно аутифицированным пользователям.
Получение публикации доступно неаутифицированному пользователяю.*

**Добавление комментария к публикации.**
```
/api/v1/posts/{post_id}/comments/
```
*Добавление комментария доступно только аутифицированному пользователю.*

**Получение, обновление, частичное обновление, удаление комментария.**
```
/api/v1/posts/{post_id}/comments/{id}/
```
*Обновить, частично обновить, удалить может только автор комментария. Доступно аутифицированным пользователям.
Получение публикации доступно неаутифицированному пользователяю.*

**Получение списка сообществ.**
```
/api/v1/groups/
```

**Получение информации о сообществе.**

```
/api/v1/groups/{id}/
```

**Получить все подписки пользователя. Отправить запрос на подписку.**

```
/api/v1/follow/
```
*Доступно только аутифицированным пользователям.*











