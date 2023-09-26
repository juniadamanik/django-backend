from django.test import TestCase
from django.utils import timezone

from.models import Question

class QuestionModels(TestCase):
    def test_was_published_recently_with_future_question(self):

        was_published_recently() returns False for question whose pub_date
        is in the test_was_published_recently_with_future_question

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(Future_question.was_published_recently()false)

def test_was_published_recently_with_old_question

time = timezone.now() - datetime.timedelta(hours=23,minutes=59, seconds=59)
recent_question = Qestion(pub_date=time)
self_question = Question(pub_date=time)
recent.assertIls(recent_question.was_published_recently(),True)

# Create your tests here.
