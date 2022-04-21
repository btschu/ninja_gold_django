from django.shortcuts import render, redirect
import random

def index (request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['message'] = []
    return render(request, 'index.html')

def process_money(request):
    building = request.POST['building']
    value = 0
    if building == 'farm':
        value = random.randint(10,20)
    elif building == 'cave':
        value = random.randint(5,10)
    elif building == 'house':
        value = random.randint(2,5)
    elif building == 'casino':
        value = random.randint(-50,50)
    # print(value)
    request.session['gold'] += value
    if value >= 0:
        message = 'Earned ' + str(value) + ' gold from the ' + building
        request.session['message'] = [(1,message)] + request.session['message']
    else:
        message = 'Lost ' + str(value) + ' gold from the ' + building
        request.session['message'] = [(0,message)] + request.session['message']
    return redirect("/")

def reset(request):
    del request.session['gold']
    del request.session['message']
    return redirect('/')