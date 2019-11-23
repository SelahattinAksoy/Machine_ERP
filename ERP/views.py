from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from .models import note
from django.contrib import messages
import speech_recognition as sr
from gtts import gTTS
import os
# Create your views here.


def index(request):

     return render(request,"index.html")


def mainpage(request):

#login page we making autontikastion for login
     if request.method=="POST":
       val1 = request.POST["username"]
       val2 = request.POST["password"]

       user=auth.authenticate(username=val1,password=val2)

       if user is not None:
           auth.login(request,user)
           return render(request, "mainpage.html")
       else:
           return redirect("/")
     else:
          return redirect("/")


#register page  düzenlemeler yap
def register(request):
    if request.method == "POST":
        val1 = request.POST["username"]
        val2 = request.POST["password"]
        val3 = request.POST["repassword"]

        if val2==val3 :
          if User.objects.filter(username=val1).exists():
              return render(request, "register.html")
          user=User.objects.create_user(username=val1,password=val2)
          user.save();
          return redirect("/")
        else:
            return render(request, "register.html")

    else:
        return render(request, "register.html")

@login_required(login_url="/mainpage/")  #buuuuuu çohhhhh önemli important requirement resmen aq :) :)
def map(request):
    return render(request, "map.html",{"numbers":range(3)})

@login_required(login_url="/mainpage/")
def databases(request):
    return render(request, "databases.html")

@login_required(login_url="/mainpage/")
def logout(request):
    auth.logout(request)
    return redirect("/")
@login_required(login_url="/mainpage/")
def notes(request):
    all_note=note.objects.all()
    if request.method == "POST":
        val1 = request.POST["notehead"]
        val2 = request.POST["note"]
        save_note=note(notehead=val1,note=val2)
        save_note.save()
        return render(request, "note.html", {"notes": all_note})
    else:
      return render(request, "note.html",{"notes": all_note})

@login_required(login_url="/mainpage/")
def chart(request):
    return render(request,"chart.html")

@login_required(login_url="/mainpage/")
def speech(request):
  text="lan bişeyler söyle"
  language = "tr"
  if request.method == "POST":
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio,language="tr")
            output = gTTS(text=text, lang=language, slow=False)
            output.save("C:/Users/selah/Desktop/TEZ/Machine-ERP/Machine_ERP/static/sound/out.mp3")

            return render(request, "speech.html", {"text": text})
        except:
            text="bişeyler söyle"


  return render(request,"speech.html",{"text":text})



#os.system("start out.mp3")