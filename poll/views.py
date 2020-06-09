from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Questions, QuestionChoice
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = {

    }
    template = 'pages/home.html'
    return render(request, template_name=template, context=context)


# user registration
def user_registration(request):
    if request.method == 'POST':
        if request.POST['txtusername'] == '' or request.POST['txtemail'] == '' or request.POST['txtpassword'] == '':
            context = {
                 'error': 'Please fill the fields..'
            }
            template = 'pages/registration_form.html'
            return render(request, template_name=template, context=context)
        else:
            try:
                user = User.objects.get(username=request.POST['txtusername'])
                if user is not None:
                    context = {
                        'error': 'User Name or Email already taken please choose another one..'
                    }
                    template = 'pages/registration_form.html'
                    return render(request, template_name=template, context=context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['txtusername'], email=request.POST['txtemail'], password=request.POST['txtpassword'])
                auth.login(request, user)
                return redirect('home')
    else:
        context = {

        }
        template = 'pages/registration_form.html'
        return render(request, template_name=template, context=context)


# user login
def user_login(request):
    if request.method == 'POST':
        if request.POST['txtusername'] == '' or request.POST['txtpassword'] == '':
            context = {
                'error': 'Please fill the fields..'
            }
            template = 'pages/registration_form.html'
            return render(request, template_name=template, context=context)
        else:
            user = auth.authenticate(username=request.POST['txtusername'], password=request.POST['txtpassword'])
            if user is not None:
                auth.login(request, user)
                if request.POST['txtnextpage']:
                    return redirect(request.POST['txtnextpage'])
                else:
                    return redirect('home')
            else:
                context = {
                    'error': 'Please check username or password'
                }
                template = 'pages/login_form.html'
                return render(request, template_name=template, context=context)
    else:
        context = {

        }
        template = 'pages/login_form.html'
        return render(request, template_name=template, context=context)


# user logout
def user_logout(request):
    auth.logout(request)
    return redirect('home')


# display poll question
def poll_question(request):
    question = Questions.objects.all()
    context = {
       'que': question
    }
    template = 'pages/poll_question.html'
    return render(request, template_name=template, context=context)


# vote page
@login_required(login_url='login')
def vote_now(request, slug):
    question = Questions.objects.get(slug=slug)
    question_choice = QuestionChoice.objects.filter(question_id=question.id)
    context = {
        'que': question,
        'choice': question_choice
    }
    template = 'pages/vote_now.html'
    return render(request, template_name=template, context=context)


# vote on particular question
def vote(request):
    if request.method == 'POST':
        choice_vote = QuestionChoice.objects.get(id=request.POST['rdchoice'])
        choice_vote.votes += 1
        choice_vote.save()
        return redirect('poll_question')


# display result
def display_result(request, id):
    qustion_result = QuestionChoice.objects.filter(question_id=id)
    question = qustion_result[0].question_id.question
    context = {
        'question': question,
        'que': qustion_result
    }
    template = 'pages/poll_result.html'
    return render(request, template_name=template, context=context)
