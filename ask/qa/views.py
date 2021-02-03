from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout as logout_

def test(request, *args, **kwargs):
        return HttpResponse('OK')
    
def logout(request):
    if request.method == 'POST':     
        logout_(request)
        return HttpResponseRedirect(request.GET.get('next', '/'))
            
    raise Http404

"""
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user != None:
                resp = HttpResponseRedirect('/') #Replace to request.next
                return resp       
    else:
        form = LoginForm()
            
    return render(request, 'login.html', {
                'form': form,
        })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user != None:
                resp = HttpResponseRedirect('/') #Replace to request.next
                return resp	
    else:
        form = SignupForm()
            
    return render(request, 'signup.html', {
                'form': form,
        })

def question(request, *args, **kwargs):
    try:
        qid = int(kwargs['id'])
        question = Question.objects.get(id = qid)
    except:
        raise Http404
        
    answers = Answer.objects.filter(question = question).order_by('-added_at').all()
        
    answerform = AnswerForm(initial={'question': question})
      
    return render(request, 'question.html', {
            'username': request.user.username,
            'answers': answers,
            'question': question,
            'answerform': answerform,
            'authenticated': request.user.is_authenticated(),
        })
        
#@login_required(login_url='/login/', redirect_field_name='next')
def answer(request):
    if request.method == 'POST':
        answer = AnswerForm(request.POST)
            
        if answer.is_valid():
            answer.user = request.user 
            answer.save()
            
        next = request.GET.get('next', '/')

        return HttpResponseRedirect(next)
        
    raise Http404


#@login_required(login_url='/login/', redirect_field_name='next')
def ask(request):
    if request.method == 'POST':
        question = AskForm(request.POST)
        if question.is_valid():
            question.user = request.user
            question = question.save()
            return HttpResponseRedirect(question.get_url())		
    else:
        question = AskForm()
            
    return render(request, 'ask.html', {
            'question': question,
        })

def popular(request):
        questions = Question.objects.order_by('-rating', '-added_at')
        
        limit = 10
        
        try:
            pagenum = int(request.GET.get('page', 1))
        except:
            raise Http404
        
        paginator = Paginator(questions, limit)
        paginator.baseurl = reverse('popular') + '?page='
        
        try:
            page = paginator.page(pagenum)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        return render(request, 'popular.html', {
                'questions': page.object_list,
                'paginator': paginator,
                'page': page,
        })

def new(request, *args, **kwargs):
        return test(request, args, kwargs)

def home(request):
        questions = Question.objects.order_by('-added_at')
        limit = 10
        
        try:
            pagenum = int(request.GET.get('page', 1))
        except:
            raise Http404
        
        paginator = Paginator(questions, limit)
        paginator.baseurl = reverse('home') + '?page='
        
        try:
            page = paginator.page(pagenum)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        return render(request, 'main_page.html', {
                'username': request.user.username,
                'paginator': paginator,
                'page': page,
        })
"""
