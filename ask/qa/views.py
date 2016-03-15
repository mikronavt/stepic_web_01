from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from models import Question

# Create your views here.



def test(request, *args, **kwargs):
    return HttpResponse('OK')

def questions_lists_all(request):
    questions = Question.objects.filter()
    questions = questions.order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'questions_last.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popular(request, *args, **kwargs):
    questions = Question.objects.filter()
    questions = questions.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'questions_popular.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def question(request, slug):
    return HttpResponse('OK')