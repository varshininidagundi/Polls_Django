import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    Question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.Question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days =1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# PS E:\goflamingo\Polls application\mywebsite> python manage.py sqlmigrate polls 0001
# BEGIN;
# --
# -- Create model Question
# --
# CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Question_text" varchar(300) NOT NULL, "pub_date" datetime NOT NULL);
# --
# -- Create model Choice
# --
# CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(300) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
# COMMIT;