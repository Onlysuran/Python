from django.shortcuts import render,redirect

# Create your views here.

from student.models import Student

#查询
def student_list(request):
    student_all = Student.objects.all()
    return render(request,'student_list.html',{'student_all':student_all})

#新增
def to_add(request):
    return render(request,'student_add.html')

def student_add(request):
    t_name = request.POST["t_name"]
    t_age = request.POST["t_age"]
    t_sex = request.POST["t_sex"]
    t_address = request.POST["t_address"]
    t_hobby_list = request.POST.getlist("t_hobby")
    t_date = request.POST["t_date"]
    t_hobby = "";
    for hobby in t_hobby_list:
        t_hobby = t_hobby + hobby + ","

    Student.objects.create(
        t_name=t_name,
        t_age=t_age,
        t_sex=t_sex,
        t_address=t_address,
        t_hobby=t_hobby,
        t_date=t_date

    )

    return redirect('/student_list/')

#修改
def to_put(request):
    id = request.GET.get('id')
    student=Student.objects.filter(t_id=id)[0]
    return render(request,'student_put.html',{'student':student})

def student_put(request):
    t_id = request.POST["t_id"]
    t_name = request.POST["t_name"]
    t_age = request.POST["t_age"]
    t_sex = request.POST["t_sex"]
    t_address = request.POST["t_address"]
    t_hobby_list = request.POST.getlist("t_hobby")
    t_date = request.POST["t_date"]
    t_hobby = "";
    for hobby in t_hobby_list:
        t_hobby = t_hobby + hobby + ","

    Student.objects.filter(t_id=t_id).update(
        t_name=t_name,
        t_age=t_age,
        t_sex=t_sex,
        t_address=t_address,
        t_hobby=t_hobby,
        t_date=t_date

    )
    return redirect('/student_list/')