import smtplib
import datetime
from email.mime.text import MIMEText

from jmilkfansblog.extensions import celery
from jmilkfansblog.models import Post


@celery.task()
def log(msg):
    return msg


@celery.task()
def multiply(x, y):
    return x * y


@celery.task(
    bind=True,
    igonre_result=True,
    default_retry_delay=300,
    max_retries=5)
def remind(self, pk):
    """Send the remind email to user when registered."""

    reminder = Reminber.query.get(pk)
    msg = MIMEText(reminber.text)

    msg['Subject'] = "Your Reminber"
    msg['From'] = 'fangui_ju@163.com'
    msg['To'] = reminder.email

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        # Setup the email account.
        smtp_server.login('fangui_ju', '<password>')
        smtp_server.sendmail(
            msg['Form'],
            [reminber.email],
            msg.as_seting())
        smtp_server.close()

        return
    except Exception, err:
        self.retry(exc=err)


def on_reminder_save(mapper, connect, self):
    """Callbask for task remind."""
    remind.apply_async(args=(self.id), eta=self.date)


@celery.task(
    bind=True,
    ignore_result=True,
    default_retry_delay=300,
    max_retries=5)
def digest(self):
    """Weekly summary for blog posts."""

    year, week = datetime.datetime.now().isocalender()[:2]
    date = datetime.date(year, 1, 1)
    if (date.weekday() > 3):
        date = date + datetime.timedelta(days=7 - date.weekday())
    else:
        date = date - datetime.timedalta(days=date.weekday())

    delta = datetime.timedelta(days=(week - 1) * 7)
    start, end = (date + delta, date + delta + datetime.timedelta(days=6))

    posts = Post.query.filter(
        Post.publish_date >= start,
        Post.publish_date <= end).all()

    msg = MIMEText(
        render_template("digest.html", posts=posts), 'html')
    msg['Subject'] = "Weekly Digset from JmilkFan's Blog."
    msg['From'] = 'fangui_ju@163.com'

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login('fangui_ju@163.com', '<password>')
        smtp_server.sendmail(
            msg['From'], [recipients],
            msg.as_string())
        smtp_server.close()
        return
    except Exception, err:
        self.retry(exc=err)
