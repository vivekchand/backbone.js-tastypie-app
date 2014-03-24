backbone.js-tastypie-app
=====================

This sample app is based on http://addyosmani.github.io/backbone-fundamentals/#exercise-2-book-library---your-first-restful-backbone.js-app except that I use tastypie for backend


Operations
==========
```
url                HTTP Method  Operation
---------------------------------------------------------------------------------------------
/api/v1/books      GET          Get an array of all books
/api/v1/books/:id  GET          Get the book with id of :id
/api/v1/books      POST         Add a new book and return the book with an id attribute added
/api/v1/books/:id  PUT          Update the book with id of :id
/api/v1/books/:id  DELETE       Delete the book with id of :id
```

Local Setup:
============
```
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
```

App Structure:
==============

```
.
|-- libraryapp
|   |-- static
|   |   |-- css
|   |   |   `-- screen.css
|   |   `-- js
|   |       |-- app.js
|   |       |-- collections
|   |       |   `-- library.js
|   |       |-- lib
|   |       |   |-- backbone-min.js
|   |       |   |-- backbone-tastypie.js
|   |       |   |-- jquery.min.js
|   |       |   `-- underscore-min.js
|   |       |-- models
|   |       |   `-- book.js
|   |       `-- views
|   |           |-- book.js
|   |           `-- library.js
|   |-- templates
|   |   `-- index.html
|   |-- api.py
|   |-- __init__.py
|   |-- models.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   `-- wsgi.py
|-- LICENSE
|-- manage.py
|-- Procfile
|-- README.md
`-- requirements.txt
```
