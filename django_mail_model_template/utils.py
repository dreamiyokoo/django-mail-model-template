from .models import MailTemplate
from typing import Dict, Any

from django.template import Context, Template
from django.core.mail import EmailMessage
from django.conf import settings


def get_mail_template(name: str, params: Dict[str, Any]) -> Dict[str, str]:
    mail_template = MailTemplate.objects.get(name=name)
    context = Context(params)
    return {
        "name": mail_template.name,
        "subject": Template(mail_template.subject).render(context),
        "body": Template(mail_template.body).render(context),
        "html": Template(mail_template.html).render(context),
    }


def send_html_mail(name: str, params: Dict[str, Any], from_email: str, to_email_list: list[str]):
    mail_template = get_mail_template(name, params)
    email = EmailMessage(
        mail_template["subject"],
        mail_template["html"],
        from_email,
        to_email_list,
    )
    email.content_subtype = "html"
    email.send()


def send_text_mail(name: str, params: Dict[str, Any], from_email: str, to_email_list: list[str]):
    mail_template = get_mail_template(name, params)
    email = EmailMessage(
        mail_template["subject"],
        mail_template["body"],
        from_email,
        to_email_list,
    )
    email.content_subtype = "plain"
    email.send()
