import smtplib
import datetime
from email.mime.text import MIMEText

from flask_mail import Message

from jmilkfansblog.extensions import flask_celery, mail
from jmilkfansblog.models import Post


@flask_celery.task(
    bind=True,
    igonre_result=True,
    default_retry_delay=300,
    max_retries=5)
def remind(self, primary_key):
    """Send the remind email to user when registered.
       Using Flask-Mail.
    """

    # Using the primary_key to get reminder object.
    # Ensure down to date from table of reminders.
    reminder = Reminber.query.get(primary_key)

    msg = MIMEText(reminber.text)
    msg = Message('fangui_ju@163.com',
                  sender="fangui_ju@163.com",
                  recipients=[reminder.email])
    msg.body = reminder.text

    mail.send(msg)


def on_reminder_save(mapper, connect, self):
    """Callback after insert table reminder."""

    remind.apply_async(args=(self.id,), eta=self.date)


@flask_celery.task(
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
