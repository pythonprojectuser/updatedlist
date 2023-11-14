from django.http import HttpResponse
from django.shortcuts import render, redirect
from form import CarlistForm
from . models import Carlist

def index(request):
    carlist=Carlist.objects.all()
    context={
        'car_list':carlist
    }
    return render(request,'index.html',context)
def detail(request,carlist_id):
    carlist=Carlist.objects.get(id=carlist_id)
    return render(request,"detail.html",{'carlist':carlist})
def add_car(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc', )
        year=request.POST.get('year', )
        img=request.FILES['img']
        carlist=Carlist(name=name,desc=desc,year=year,img=img)
        carlist.save()
    return render(request,'add.html')
def update(request: object, id):
    carlist=Carlist.objects.get(id=id)
    form = CarlistForm()
    if request.method == 'POST' and  form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'carlist':carlist})
def delete(request,id):
    if request.method=="POST":
        carlist=Carlist.objects.get(id=id)
        carlist.delete()
        return redirect('/')
    return render(request,'delete.html')
