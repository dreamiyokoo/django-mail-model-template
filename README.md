# INSTALL

```shell
pip install git+https://github.com/dreamiyokoo/django-mail-model-template.git
```

# Django settings

```python
INSTALLED_APPS = [
...
'django_mail_model_template',
]
```

# Migrations

Migrations are a way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your
database schema. They are designed to be mostly automatic, but you'll need to know when to make migrations, when to run
them, and the common issues you might run into.

You can create migrations for your application using the following command:

```shell
python manage.py makemigrations
```

This command will detect changes made to your models and generate the appropriate migrations.

Once the migrations have been created, you can apply them to your database using:

```shell
python manage.py migrate
```

This command applies the migrations and updates the database schema.

# Viewing Migrations in the Admin

Django's admin interface allows you to view the state of applied migrations. To do this, follow these steps:

1. Log in to the Django admin interface.
2. Navigate to the **"Migrations"** section, which is available under the "Django" admin area.
3. Here, you will be able to see a list of migrations and their states (applied or unapplied).

By using these tools, you can manage the evolution of your database schema in a controlled and predictable way.

# Usage

Register the template either via django-admin or through code.

```python
from django_mail_model_template.models import MailTemplate

MailTemplate.objects.create(
    name="main",
    subject="main subject {{ name }}",
    body="main body {% if name %}{{ name }}{% endif %}",
    html="<p>main html {{ name }}</p>",
)
```

```python
from django_mail_model_template.utils import get_mail_template
params = {"name": "yamada"}
result = get_mail_template("main", params)
```

## send html mail

```python
from django_mail_model_template.utils import send_html_mail
params = {"name": "yamada"}
send_html_mail("main", params, "from@example.com",["to@example.com"])
```

## send text mail

```python
from django_mail_model_template.utils import send_text_mail
params = {"name": "yamada"}
send_text_mail("main", params, "from@example.com",["to@example.com"])
```
