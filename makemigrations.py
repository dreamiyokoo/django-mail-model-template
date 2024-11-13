import os
import django
from django.core.management import call_command

# Djangoプロジェクトの設定モジュールを設定
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

# Djangoを初期化
django.setup()

# makemigrationsコマンドを呼び出す
call_command('makemigrations')