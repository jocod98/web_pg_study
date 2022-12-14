from django.shortcuts import render
from .models import Question
# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = Question.object.get(id = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
    #RENDER함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수.
    #템플릿파일이란 HTML 파일과 비슷하지만 파이썬 파일을 불러서 사용할 수 있는 HTML파일이다.
     
