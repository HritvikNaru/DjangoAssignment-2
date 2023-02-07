import threading
from django.core.mail import send_mail
import time
class EmailThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        try:
            time.sleep(3)
            send_mail(
                'Subject',
                'Body',
                'hritvik@attentive.ai',
                ['hritvik10@gmail.com'],
                fail_silently=False,
        )
        except Exception as e:
            print(e)


