from django.db import models


class Question(models.Model):
  question_text = models.CharField(max_length=180)
  pub_date = models.DateTimeField()

  def __str__(self):
    return self.question_text
