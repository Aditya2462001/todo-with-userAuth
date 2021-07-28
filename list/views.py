from django.shortcuts import redirect, render ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from .models import *

# Create your views here.

def index(request):
    if request.user.is_active:
        done_todo = 0
        not_done = 0
        author = Author.objects.get(author = request.user)
        all_todo = ToDo.objects.all()
        all_todo = all_todo.filter(author = author)
        len_todo = len(all_todo)
        for i in all_todo :
            if i.done == True:
                done_todo += 1
            else:
                not_done += 1

        context = {
            "all_todo":all_todo,
            "author":author,
            "total_todo":len_todo,
            "done_todo":done_todo,
            "not_done":not_done,
        }

    else:
        return redirect('login/')
    return render(request,"index.html",context)


def save_content(request):
    if request.user.is_active:
        if request.method == "POST":
            author = Author.objects.get(author = request.user)
            content = request.POST.get('content')
            todo = ToDo(author = author , content = content)
            todo.save()
            return redirect('/')
    else:
        return redirect('login/')

def edit_content(request,pk):
    if request.user.is_active:
        todo = ToDo.objects.get(id = pk)
        
        if request.method == "POST":
            edited_content = request.POST.get('content')
            todo.content = edited_content
            todo.save()
            return redirect('/')
        return render(request,"edit.html",{"content":todo})
    else:
        return redirect('login/')

def delete_todo(request,pk):
    if request.user.is_active :
        todo = ToDo.objects.get(id = pk)
        todo.delete()
        return redirect('/')
    else:
        return redirect('login/')

def done_todo(request,pk):
    if request.user.is_active:
        todo = ToDo.objects.get(id = pk)
        todo.done = True 
        todo.save()
        print(todo.done)
        return redirect('/')
    else:
        return redirect('login/')




def view_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user is not None:
            if user.is_active :
                login(request,user)
                return redirect('/') 
        else:
            messages.info(request,"Wrong Input")
            return render(request,"login.html")

    return render(request,"login.html")





def view_register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        image =  request.FILES.get('image')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordv = request.POST.get('vpassword')
        if password != passwordv:
            messages.info(request,"Password not match!!!")
            return render(request,"register.html")

        if User.objects.filter(username = username).exists():
            messages.info(request,"User Name is exist plese try another")
            return render(request,"register.html")

        user = User( first_name = fname , last_name = lname , email = email ,username=username )
        user.set_password(password)
        user.save()

        print("sucessfully added in the database")
        author = Author(author = user , name = fname , lname = lname , email = email , number = number ,image = image)
        author.save()
        messages.info(request,"You successfully Created your Account Please log in ")
        return render(request,"register.html")
        
    return render(request,"register.html")
    

def view_logout(request):
    if request.user.is_active:
        logout(request)
        print("logout successuflly!!!")
        return redirect('login/')
    else:
        return redirect('login/')
    return render(request,"logout.html")
