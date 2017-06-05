# _*_ encoding:utf-8 _*_

from random import choice
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from muxue.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    for i in xrange(randomlength):
        str += choice(chars)
    return str


def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = u"慕学网注册"
        email_body = u"请点击下面的链接激活你的账号: http://192.168.20.64:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass



