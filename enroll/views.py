from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

#Function to add and show data..
def add_student(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration() 
    
    stud = Student.objects.all()  
    return render(request, 'addandshow.html', {'form':fm, 'stu':stud})


#Function to delete data...
def data_del(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#Function to edit/update..
def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
          fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)      
    return render(request, 'updateanddelete.html', {'form': fm})
   
    
    

  
  