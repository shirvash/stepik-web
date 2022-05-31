from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Question, Answer
from .forms import AnswerForm, AskForm


# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new(request, *args, **kwargs):
    return test(request, args, kwargs)


def new_questions(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {'questions': page.object_list, 'paginator': paginator, 'page': page})


def popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {'questions': page.object_list, 'paginator': paginator, 'page': page})


def question(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question=id)
    user = request.user
    if request.method == 'POST':
        form = AnswerForm(user, request.POST, initial={'question': question.id})
        if form.is_valid():
            answer = form.save()
    else:
        form = AnswerForm(user, initial={'question': question.id})
    return render(request, 'question.html', {'question': question, 'answers': answers, 'form': form})


def ask(request):
    if request.method == 'POST':
        user = request.user
        form = AskForm(user, request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'signup.html', {'error': 'This name is busy'})
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render(request, 'signup.html')


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login or password'})
    else:
        return render(request, 'login.html')
