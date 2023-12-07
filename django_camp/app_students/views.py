from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect 
from app_students.models import StudentInfo
from app_students.forms import StudentModelForm
from django.urls import reverse
from sweetify import sweetify
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app_students/home.html')

def student(request):
    all_data = StudentInfo.objects.all()
    context = {'all_data' : all_data}
    return render(request, 'app_students/student.html', context)

def student_add(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'คุณกรอกข้อมูลสำเร็จ', text='เราได้บันทึกข้อมูลของคุณแล้ว!', persistent='OK!')
            return HttpResponseRedirect(reverse('student'))
        else:
            sweetify.error(request, 'เกิดข้อผิดพลาด', text='คุณกรอกข้อมูลไม่ครบหรือชื่อซ้ำกัน', persistent='OK!')
    else:
        form = StudentModelForm()
    context = {'form' : form }
    return render(request, 'app_students/components/student_add.html', context)

def student_edit(request, pk):

    student = StudentInfo.objects.get(id=pk)
    form = StudentModelForm(instance=student)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'คุณแก้ไขข้อมูลสำเร็จ', text='เราได้บันทึกข้อมูลของคุณแล้ว!', persistent='OK!')
            return HttpResponseRedirect(reverse('student'))
        else:
            sweetify.error(request, 'เกิดข้อผิดพลาด', text='คุณกรอกข้อมูลไม่ครบหรือชื่อซ้ำกัน', persistent='OK!')

    context = {'form' : form }
    return render(request, 'app_students/components/student_add.html', context)

def student_delete(request, pk):
    student = StudentInfo.objects.get(id=pk)
    student.delete()
    sweetify.success(request, 'Deleted!', text='เราได้ลบข้อมูลของคุณแล้ว!', persistent='OK!')
    return HttpResponseRedirect(reverse('student'))


def contact(request):
    return render(request, 'app_students/contact.html')