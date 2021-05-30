from django.shortcuts import render,redirect

# Create your views here.
from book.models import Book

#查询
def book_list(request):
    book_add=Book.objects.all()
    return render(request,'book_list.html',{'book_add':book_add})

#新增
def to_add(request):
    return render(request,'book_add.html')

def book_add(request):
    t_name=request.POST["t_name"]
    t_price=request.POST["t_price"]
    t_type_list=request.POST.getlist("t_type")
    t_type = ""
    for type in t_type_list:
        t_type = t_type + type + ","
    t_publisher=request.POST["t_publisher"]
    t_date=request.POST["t_date"]
    t_updown=request.POST["t_updown"]

    Book.objects.create(
        t_name=t_name,
        t_price=t_price,
        t_type=t_type,
        t_publisher=t_publisher,
        t_date=t_date,
        t_updown=t_updown
    )

    return redirect('/book_list/')


#删除
def book_dele(request):
    id=request.GET.get("id")
    Book.objects.filter(t_id=id).delete()
    return redirect('/book_list/')

#修改
def to_put(request):
    id = request.GET.get("id")
    book=Book.objects.filter(t_id=id)[0]
    return render(request, 'book_put.html', {'book': book})

def book_put(request):
    t_id = request.POST["t_id"]
    t_name = request.POST["t_name"]
    t_price = request.POST["t_price"]
    t_type_list = request.POST.getlist("t_type")
    t_type = ""
    for type in t_type_list:
        t_type = t_type + type + ","
    t_publisher = request.POST["t_publisher"]
    t_date = request.POST["t_date"]
    t_updown = request.POST["t_updown"]

    Book.objects.filter(t_id=t_id).update(
        t_name=t_name,
        t_price=t_price,
        t_type=t_type,
        t_publisher=t_publisher,
        t_date=t_date,
        t_updown=t_updown
    )

    return redirect('/book_list/')