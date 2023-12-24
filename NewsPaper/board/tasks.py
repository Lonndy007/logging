from celery import shared_task
import time
from NewsPaper.news.models import Post
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task()
def news(text,subcribers):
    last_news = Post.objects.all().order_by('-time')[:5]
    html_content = render_to_string(
        'daily_post.html',
        {
            'text': text,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }

    )

    msg = EmailMultiAlternatives(subject=last_news, body='', from_email=settings.EMAIL_HOST_USER, to=subcribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
