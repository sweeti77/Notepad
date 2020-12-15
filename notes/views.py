from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from django.db import IntegrityError

from .forms import NoteForm
from .models import Note


# Create your views here.
def index(request):
    return render(request, 'index.html')

def homePage(request):
    obj = Note.objects.filter(user = request.user)
    return render(request, 'homePage.html', {'notes':obj})

def create_note(request):
    if request.method == "GET":
        return render(request, 'createnotes.html', {'form':NoteForm()})
    else:
        try:
            form = NoteForm(request.POST)
            newNote = form.save(commit=False)
            newNote.user = request.user
            newNote.save()
            return redirect('homePage')
        except ValueError:
            return render(request, 'createnotes.html', {'form':NoteForm(), 'error':"Bad Inputs"})


def update_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk,user=request.user)
    if request.method == "GET":
        form = NoteForm(instance=note)
        return render(request, 'update_notes.html', {'form':form, 'note':note})
    else:
        try:
            form = NoteForm(request.POST, instance=note)
            form.save(commit=False)
            return redirect('homePage')
        except ValurError:
            return render(request, 'update_notes.html', {'form':form, 'error':"Bad Inputs", 'note':note})


def delete_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk,user=request.user)
    if request.method == "POST":
        note.delete()
    return redirect('homePage')






#Views for Authentication

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('index')


def loginUser(request):
    if request.method=="GET":
        return render(request, 'login.html', {'form':AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, username=User.objects.get(email=username), password=password)
        except:
            user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'form':AuthenticationForm(), 'error':"Bad Inputs. Please Try Again."})
        else:
            login(request, user)
            return redirect("homePage")


def signupUser(request):
    if request.method=="GET":
        return render(request, 'signup.html',{'form':SignupForm()})
    else:
        #create new user
        try:
            if request.POST['password1']==request.POST['password2']:
                user = User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password1'])
                user.save
                login(request,user)
                return redirect('homePage')
            else:
                return render(request, 'signup.html',{'form':SignupForm(),
                        'error':"Passwords donot match. Try Again"})

        except IntegrityError:
            return render(request, 'signup.html',{'form':SignupForm(),
                        'error':"Username Already Taken. Try Again"})
