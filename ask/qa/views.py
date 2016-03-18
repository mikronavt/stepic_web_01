from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from models import Question, Answer
from forms import AnswerForm, AskForm, SignupForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.context_processors import csrf
#import django.middleware.csrf.CsrfViewMiddleware
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

default_url = 'http://0.0.0.0/'


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

@csrf_protect
def question_details(request, qid):

    question = get_object_or_404(Question, id=qid)
    answers = Answer.objects.filter(question_id=qid)
    form = AnswerForm()

    return render(request, 'question_details.html', {
        'title': question.title,
        'qtext': question.text,
        'answers':answers,
        'form':form,
    })

@csrf_protect
def ask(request):

    if request.method == 'POST':
        if request.user.is_authenticated():
            return HttpResponse('OK')
            form = AskForm(request.POST)
            form._user = request.user
            if form.is_valid():
                question = form.save()

                url = question.get_url()

                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(default_url)
    else:
        form = AskForm(request.user)
    return render(request, 'ask_form.html',{
            'form':form,
        })

@csrf_protect
def answer(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = AnswerForm(request.POST)
            form._user = request.user
            if form.is_valid():
                answer = form.save()
                question = answer.question
                url = question.get_url()
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(default_url)
    else:
        form = AnswerForm(request.user)
    return render(request, 'answer_form.html',{
            'form':form,
        })

@csrf_protect
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        response = HttpResponseRedirect(default_url)
        return response
 #       username = request.POST.get('username')
  #      password = request.POST.get('password')
  #      session = do_login(username, password)
   #     if session:
    #        sessid = session.key
     #       response = HttpResponseRedirect(default_url)
      #      response.set_cookie('sessid', sessid,
       #         domain=default_url, httponly=True,
        #        expires = session.expires,
         #   )
          #  return response
    return render(request, 'login_form.html',{
            'form':form,
        })

@csrf_protect
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        response = HttpResponseRedirect(default_url)
        return response
            #session = do_login(username, password)
            #if session:
            #    sessid = session.key
            #    response = HttpResponseRedirect(default_url)
            #    response.set_cookie('sessid', sessid,
            #        domain=default_url, httponly=True,
            #        expires = session.expires,
            #    )
            #    return response
    return render(request, 'signup_form.html',{
            'form':form,
        })