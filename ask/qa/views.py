from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logout_
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.views.decorators.http import require_GET

from .forms import AskForm, AnswerForm
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new(request, *args, **kwargs):
    return test(request, args, kwargs)


@require_GET
def home(request):
    qu_list = Question.objects.order_by('-added_ad')

    paginator = Paginator(qu_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'questions': questions})


@require_GET
def popular(request):
    qu_list = Question.objects.order_by('-rating')

    paginator = Paginator(qu_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'questions': questions})


def question(request, qu_id):
    qu = get_object_or_404(Question, pk=qu_id)
    answers = Answer.objects.filter(question=qu)
    form = AnswerForm(initial={'question': qu_id})
    return render(request, 'question.html', {'question': qu, 'answers': answers, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        #form._user = request.user.id
        if form.is_valid():
            qu = form.save()
            return redirect(qu.get_absolute_url(), qu.pk)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        #form._user = request.user.id
        if form.is_valid():
            ask = form.save()
            return redirect(ask.question.get_absolute_url(), ask.question.id)
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form})


def signup(request):
    return HttpResponse('OK')
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         us = authenticate(username=request.POST['username'], password=request.POST['password'])
    #         login(request, us)
    #         return redirect('/')
    # else:
    #     form = SignupForm()
    # return render(request, 'signup.html', {'form': form})


def logout(request):
    return HttpResponse('OK')
    # if request.method == 'POST':
    #     logout_(request)
    #     return HttpResponseRedirect(request.GET.get('next', '/'))
    #
    # raise Http404


def login_(request):
    return HttpResponse('OK')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save(request)
#             if user != None:
#                 resp = HttpResponseRedirect('/')  # Replace to request.next
#                 return resp
#     else:
#         form = LoginForm()
#
#     return render(request, 'login.html', {
#         'form': form,
#     })