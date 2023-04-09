from django.shortcuts import render, HttpResponse,redirect
from .models import *
import bcrypt
from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"login.html")


def registeruser(request):    
    
    errors=Userr.objects.basic_validator(request.POST)
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/')
            
    
    
    first_name=request.POST['firstname']
    last_name=request.POST['lastname']
    emailform=request.POST['email']
    passwordd = request.POST['password']
    password2 = request.POST['password2']
   
    if password2 != passwordd:
        messages.error(request, 'Passwords do not match.')
    
    
    pw_hash = bcrypt.hashpw(passwordd.encode(), bcrypt.gensalt()).decode()    
  
    Userr.objects.create(firstname=first_name,lastname=last_name,email=emailform,password=pw_hash) 
    return redirect("/")    

def loginuser(request):
     user = Userr.objects.filter(email=request.POST['email'])
     if user:
         logged_user = user[0]
         if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
             request.session['userid'] = logged_user.id
             return redirect('/homepage')
     return redirect('/')
 
def  homepage(request):
    user_id=request.session.get('userid')
    user=Userr.objects.get(id=user_id)
    
    context={
        'id':user_id,
        'firstname':user.firstname,
        'lastname':user.lastname,
        'onefilm':Film.objects.all()
         
           
    }
     
    return render(request,"home.html",context)


def addfilm(request):
    return render(request,"newfilm.html")

def addnewfilm(request):
    
  errors=Film.objects.basic_validator(request.POST)
  if len(errors)>0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/addnewfilm')
 
  film_name=request.POST['name']
  film_dis=request.POST['description']
  film_date=request.POST['release-date']
  film_network=request.POST['network']
  film_adder=request.session.get('userid')
  Film.objects.create(filmname=film_name,filmdiscription=film_dis,filmnetwork=film_network,filmdate=film_date,filmadder_id=film_adder)
  return redirect('/homepage')

def log_out(request):
        request.session.clear()
        return redirect('/')
  
def showfilm(request,pk):
    context={
        'film':Film.objects.get(id=pk)
        
    }
    return render(request,"showfilm.html",context)

def deletefilm(request,pk):
    film=Film.objects.get(id=pk)
    film.delete()
    return redirect('/homepage')

def editfilm(request,pk):
    context={
        'film':Film.objects.get(id=pk)
    }
    return render(request,"editfilm.html",context)
def makeedit(request,pk):
    filmnamepost=request.POST['name']
    filmdiscriptionpost=request.POST['description']
    filmdatepost=request.POST['release-date']
    filmnetworkpost=request.POST['network']
    
    film=Film.objects.get(id=pk)
    film.filmname=filmnamepost
    film.filmdiscription=filmdiscriptionpost
    film.filmdate=filmdatepost
    film.filmnetwork=filmnetworkpost
    film.save()
    return redirect('homepage')

    
    return redirect('/homepage')