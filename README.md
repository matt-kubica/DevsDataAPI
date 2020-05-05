# DevsDataAPI

Simple API created for DevsData interview.
Endpoints:
* `/event` [POST, GET] (json) - allows posting new event, as well getting info about all available events
* `/event/<int:id>` [GET] (json) - allows getting info about one particular event
* `/event/thumbnail` [POST] (multipart / form) - uploading thumbnail for existing event
* `/registration` [POST, DELETE] (json) - post allows to register for particular event, in response uuid code is returned, delete allows canceling registration only if conditions are approperiate

Running (being in project root):
* `pipenv shell`
* `pipenv update`
* `python manage.py makemigrations management`
* `python manage.py migrate`
* `python manage.py runserver`
