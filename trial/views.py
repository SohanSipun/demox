from django.shortcuts import render
from .forms import StudentForm
from .models  import StudentModel
# Create your views here.
def studentview(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            print(fm.errors)
    else:
        fm=StudentForm()
    stud=StudentModel.objects.all()
    return render(request,'registration.html',{'form':fm,'student':stud})
