from django.shortcuts import render,redirect

# Create your views here.
from .forms import *

from event.models import *
from django.contrib.auth.decorators import login_required
from users import views
from users.models import *



def studentregistered(request,title):
    club = request.session['club']
    student = eventregmodel.objects.all().filter(event_title=title)
    return render(request,'student.html',{'form':student,'club':club} )


def general_reg(request):
    club = request.session['club']
    if request.method=='POST':
        form=eventcreateForm(request.POST)
        form.club = club
        print(form.club," yoy")
        #club = request.POST.get('club')
        newform = general.objects.all().filter(club = club)
        if form.is_valid():
            print("HEllo")
            form.save()
            return redirect('homeadmin')
    else:
        form=eventcreateForm(initial={'club': club})
        
    #redirect to workshop_reg url    
    return render(request,'a_workshops.html',{'form':form})



def hackathons(request):

    club = request.session['club']
    hacks=general.objects.all().filter(club=club)
    length=len(hacks)
    
    return render(request,'index-0.html',{'hacks':hacks,'length':length})




def update_general(request,pk):

    hack=general.objects.get(id=pk)  ### event
    print(hack)
    form=eventcreateForm(instance = hack)
    newform = general.objects.filter(club = hack.club)  ## organising club
    if request.method=='POST':
        form=eventcreateForm(request.POST,instance=hack)
        if form.is_valid():
            print("shivaji cool")
            form.save()
            return redirect('homeadmin')
    

    return render(request,'hack_update.html',{'form':form})







def delete_general(request,pk):

    hack=general.objects.get(id=pk)

    if request.method=='POST':
        hack.delete()
        return redirect('homeadmin')
            
    

    return render(request,'hack_delete.html',{'item':hack})

