from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from models import Question, Answer

# Create your views here.



def test(request, *args, **kwargs):
    return HttpResponse('OK')

def questions_all(request, *args, **kwargs):
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

def popular_list(request, *args, **kwargs):
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

def question_details(request, slug):

    #question = get_object_or_404(Question, slug=slug)
    #question = Question.objects.get(slug=slug)
    return slug
    #answers = Answer.objects.filter(question_id=question.id)

    #return render(request, 'question_details.html', {
        #'question': question,
        #'answers':answers.object_list,
    #})
