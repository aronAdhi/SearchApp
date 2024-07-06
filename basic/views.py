from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render

def basic(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('first_page.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def ram(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('ram.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def krishna(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('krishna.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))  

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def say_hello(request, name):
    data = [
        ['Sun, Moon, earth, sun, sun, sun, jupiter, saturn, uranus', 'Moon', 'Ragu','Mars'],
        ['Kedhu', 'Sani'],
        ['', ''],
        ['Guru', 'Budha', 'Venus'],
    ]
    lak = 4
    return render(request, 'hello.html', {'name': data, 'lakana': lak})


def overall(request):
  data1 = [
        ['Sun, Moon, Ragu', 'Moon', 'Earth', 'Sun'],
        ['Moon', 'Rahu', 'Mars'],
        ['Ketu', 'Sani'],
        ['', ''],
        ['Guru', 'Budha', 'Venus'],
    ]
  data_sets = [
        {'name': data1, 'lakana': 4}
    ] 
  item_list = [['first', [1, 2, 3, ['this', 'should', 'create', 'next', 'list']]], ['second', []], ['third', [3]]]  # Example list of lists
  return render(request, 'overall.html', {'item_list': item_list, 'data_sets': data_sets})