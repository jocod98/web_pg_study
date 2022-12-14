from django.db import models

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)
    #길이 제한있는 텍스트는 CharField
    content = models.TextField()
    #제한없는 텍스트는 TextField 
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    # on_delete = CASCADE 는 질문 삭제 --> 답변도 삭제 한다는 뜻.

    content = models.TextField()
    create_date = models.DateTimeField()
