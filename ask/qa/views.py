from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from models import Question, Answer
from forms import AnswerForm, AskForm

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

def question_details(request, qid):

    question = get_object_or_404(Question, id=qid)
    answers = Answer.objects.filter(question_id=qid)


    return render(request, 'question_details.html', {
        'title': question.title,
        'qtext': question.text,
        'answers':answers,
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask_form.html',{
            'form':form,
        })


def answer(request):
    return HttpResponse('OK')