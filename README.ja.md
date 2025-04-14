# インストール

```shell
pip install django-mail-model-template
```

# Django設定

```python
INSTALLED_APPS = [
...
'django_mail_model_template',
]
```

# マイグレーション

マイグレーションとは、モデルに加えた変更（フィールドの追加、モデルの削除など）をデータベーススキーマに反映させる方法です。これらは基本的に自動化されていますが、マイグレーションを作成するタイミング、実行するタイミング、および発生する可能性がある一般的な問題を知っておく必要があります。

以下のコマンドを使用して、アプリケーションのマイグレーションを作成できます：

```shell
python manage.py makemigrations
```

このコマンドはモデルに加えられた変更を検出し、適切なマイグレーションを生成します。

マイグレーションが作成されたら、以下のコマンドを使用してデータベースに適用できます：

```shell
python manage.py migrate
```

このコマンドはマイグレーションを適用し、データベーススキーマを更新します。

# 管理画面でのマイグレーション表示

Djangoの管理インターフェースでは、適用されたマイグレーションの状態を表示できます。以下の手順に従ってください：

1. Django管理インターフェースにログインします。
2. 「Django」管理エリアの下にある「**マイグレーション**」セクションに移動します。
3. ここで、マイグレーションのリストとその状態（適用済みまたは未適用）を確認できます。

これらのツールを使用することで、データベーススキーマの進化を制御可能で予測可能な方法で管理できます。

# 使用方法

テンプレートはdjango-adminを介して、またはコードを通じて登録します。

```python
from django_mail_model_template.models import MailTemplate

MailTemplate.objects.create(
    name="main",
    subject="メインの件名 {{ name }}",
    body="メインの本文 {% if name %}{{ name }}{% endif %}",
    html="<p>メインのHTML {{ name }}</p>",
)
```

```python
from django_mail_model_template.utils import get_mail_template
params = {"name": "山田"}
result = get_mail_template("main", params)
```

## HTMLメールの送信

```python
from django_mail_model_template.utils import send_html_mail
params = {"name": "山田"}
send_html_mail("main", params, "from@example.com",["to@example.com"])
```

## テキストメールの送信

```python
from django_mail_model_template.utils import send_text_mail
params = {"name": "山田"}
send_text_mail("main", params, "from@example.com",["to@example.com"])
```

# 多言語サポート

## 異なる言語のテンプレートの設定

`language`フィールドを指定することで、異なる言語のテンプレートを作成できます：

```python
from django_mail_model_template.models import MailTemplate

# 英語テンプレート
MailTemplate.objects.create(
    name="welcome",
    subject="Welcome {{ name }}",
    body="Hello {{ name }}, welcome to our service!",
    html="<p>Hello {{ name }}, welcome to our service!</p>",
    language="en"  # ISO 639-1言語コード
)

# 日本語テンプレート
MailTemplate.objects.create(
    name="welcome",
    subject="ようこそ {{ name }}さん",
    body="こんにちは、{{ name }}さん。当サービスへようこそ！",
    html="<p>こんにちは、{{ name }}さん。当サービスへようこそ！</p>",
    language="ja"
)
```

## 言語指定でテンプレートを使用する

テンプレートを取得する際に言語を指定できます：

```python
from django_mail_model_template.utils import get_mail_template

# 英語のテンプレートを取得
params = {"name": "John"}
result = get_mail_template("welcome", params, language="en")

# 日本語のテンプレートを取得
params = {"name": "山田"}
result = get_mail_template("welcome", params, language="ja")
```

指定した言語でテンプレートが利用できない場合、デフォルト言語（`settings.LANGUAGE_CODE`で指定）にフォールバックします。それも利用できない場合は英語にフォールバックします。

# 戻り値に関する重要な注意

バージョンX.X.Xより、`get_mail_template()`は辞書の代わりに`MailTemplateParams`オブジェクトを返すようになりました。辞書の表記法ではなく、属性表記法を使用して値にアクセスしてください：

```python
# 古い（辞書）構文 - もう動作しません
result = get_mail_template("welcome", params)
subject = result["subject"]
body = result["body"]

# 新しい（オブジェクト）構文 - 現在の使用法
result = get_mail_template("welcome", params)
subject = result.subject
body = result.body
html = result.html
name = result.name
```

`MailTemplateParams`オブジェクトには以下の属性があります：
- `name`：テンプレートの名前
- `subject`：レンダリングされた件名
- `body`：レンダリングされたプレーンテキスト本文
- `html`：レンダリングされたHTML本文

# モデル設定に関する注意

このライブラリを複数の言語で使用する場合、`MailTemplate`モデルの`name`フィールドに`unique=True`が設定されていないことを確認してください。これがあると、異なる言語で同じテンプレート名を作成できなくなります。モデルでは代わりに`name`と`language`フィールドに対して`unique_together`を使用するべきです。