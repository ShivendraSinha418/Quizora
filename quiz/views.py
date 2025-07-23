from django.shortcuts import render
from .quiz_data import ques_list
from .quiz_sol import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def quiz(request):
    return render(request,'quiz.html')
def play(request):
    sub = request.GET.get('data')
    sol = sub.replace(' ','_')
    request.session['sol'] = sol
    request.session['sub'] = sub
    context ={
        'questions':ques_list[sub],
        'options': Options[sol]
    }
    return render(request,'play.html',context)
def showResult(request):
    sol_list =[]
    sol = request.session.get('sol')
    sub = request.session.get('sub')
    if(request.method == 'POST'):
        for i in range(20):
            sol_list.append(request.POST.get(f'option{i}'))
        context ={
            'ques' : ques_list[sub],
            'correctopt' : Options[sol],
            'selectedopt' : sol_list,
        }
    return render(request,'result.html',context)