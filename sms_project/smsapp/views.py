from django.shortcuts import render,redirect
from .models import StudentModel
from .forms import StudentForm

def home(request):
	data = StudentModel.objects.all()
	return render (request,'home.html',{'data':data})

def create(request):
	if request.method=="POST":
		f = StudentForm(request.POST)
		if f.is_valid():
			f.save()
			fm = StudentForm()
			return render(request,'create.html',{'fm':fm,'msg':'Record added'})
		else:
			return render(request,'create.html',{'fm':f,'msg':'Check errors'})
	else:
		fm = StudentForm()
		return render(request,'create.html',{'fm':fm})

def delete(request,id):
	ds = StudentModel.objects.get(rno=id)
	ds.delete()
	return redirect('home')

def edit(request,id):
	et = StudentModel.objects.get(rno=id)
	fm = StudentForm(initial={'rno':et.rno,'name':et.name,'marks':et.marks})
	fm.fields['rno'].widget.attrs['readonly']=True
	return render(request,'update.html',{'fm':fm})

def update(request):
	if request.method=="POST":
		
		r = request.POST.get("rno")	
		n = request.POST.get("name")
		m = request.POST.get("marks")	
		s = StudentModel.objects.get(rno=r)
		s.name = n 
		s.marks = m
		s.save()
		fm = StudentForm()
		return render(request,'update.html',{'fm':fm,'msg':'Record Updated'})
	else:
		fm = StudentForm()
		return render(request,'update.html',{'fm':fm})