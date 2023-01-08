from django.shortcuts import render
from todo.models import todo_list
from django.http import HttpResponseRedirect
from django.urls import reverse
from todo.forms import addingtodo

def todo(requests):
    form = addingtodo()
    dat = todo_list.objects.order_by('date')
    if requests.method=='POST':
        form = addingtodo(requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))


    return render(requests,'todo/home.html',{'form':form,'data':dat})

def ondelete(requests,pk):
    dat = todo_list.objects.get(pk=pk)
    dat.delete()
    return HttpResponseRedirect(reverse('home'))
    
