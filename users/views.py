from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
# Create your views here.

from .forms import *
from .models import *
from accounts.views import *


def user_profile(request):
    user = request.session['user']
    #hack = general.objects.get(id=pk)
    new = UserReg.objects.get(username=user)
    email = new.email
    userevent = eventregmodel.objects.all().filter(email = email)
    return render(request,"profile.html",{'form':userevent,'email':email,'user':user})



def login_u(request):
    
    if request.method == 'POST':
        print("cool ",request.method)
        form = login_user_form(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            request.session['user']=user
            username = request.session['user']
            print(username)
            try:
                if UserReg.objects.filter(username = user , password1 = passw):
                    yo = True
                else:
                    yo = False
                
            except:
                yo = False
            print(yo)
            if yo:
                return redirect('user_profile')

            else:
                form = login_user_form()
                return render(request,"login_user.html",{"form":form})
        else:
            form = login_user_form()
            return render(request,"login_user.html",{"form":form})

    else:
        form = login_user_form()
        return render(request,"login_user.html",{"form":form})

   

def login_a(request):
    if request.method == 'POST':
        print("cool ",request.method)
        form = login_admin_form(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("club")
            passw = form.cleaned_data.get("password")
            request.session['club'] = user
            club = request.session['club']
            print(club)
            #print(user,passw)
            try:
                if AdminReg.objects.filter(club = user , password1 = passw):
                    yo = True
                else:
                    yo = False
                
            except:
                yo = False
            print(yo)
            if yo:
                return redirect('homeadmin')

            else:
                form = login_admin_form()
                return render(request,"login_admin.html",{"form":form})
        else:
            form = login_admin_form()
            return render(request,"login_admin.html",{"form":form})

    else:
        form = login_admin_form()
        return render(request,"login_admin.html",{"form":form})



def pass_check_admin(request):
    if request.method=='POST':
        form=AdminRegForm(request.POST)
        if form.is_valid():
            print("hello")
            club =  form.cleaned_data.get('club')
            print(club)
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1==pass2:
                yo = AdminReg.objects.filter(club=club).first()
                print(yo)
                if yo:
                    yo = True
                else:
                    yo = False
            
                if yo:
                    print("sab chutiye")
                    messages.info(request, "Username already exist , try another name")
                    form = AdminRegForm()
                    return render(request,"register_admin.html",{'form':form})
                        
                else:
                    form.save()
                    return redirect('admin')

            else:
                messages.info(request, "Password doesnt match!")
                form = AdminRegForm()
                return render(request,"register_admin.html",{'form':form})
        else:
            form = AdminRegForm()
            return render(request,"register_admin.html",{'form':form})

    else:
        form = AdminRegForm()
        return render(request,"register_admin.html",{'form':form})





def pass_check_user(request):
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            print("hello")
            user =  request.POST.get("username")
            pass1 = request.POST.get("password1")
            pass2 = request.POST.get("password2")
            email=  request.POST.get("email")
            if pass1==pass2:
                try:
                    yo = UserReg.objects.get(username=user)
                    fo = UserReg.objects.get(email=email)
                    yo = True
                    fo= True
                except:
                    yo = False
                    fo=  False
                print(yo)
                if yo:
                    print("sab chutiye")
                    messages.info(request, "Username already exist , try another name")
                    form = UserRegForm()
                    return render(request,"register_user.html",{'form':form})

                elif fo:
                    messages.info(request, "Email already exist , try another email")
                    form = UserRegForm()
                    return render(request,"register_user.html",{'form':form})

                else:
                    form.save()
                    return redirect('user')

            else:
                messages.info(request, "Password doesnt match!")
                form = UserRegForm()
                return render(request,"register_user.html",{'form':form})
        else:
            form = UserRegForm()
            return render(request,"register_user.html",{'form':form})

    else:
        form = UserRegForm()
        return render(request,"register_user.html",{'form':form})


def eventreg(request,pk):
    hack = general.objects.get(id=pk)
    eventtitle = hack.title
    #print(hack.club)
    user = request.session['user']   ### mohit
    cur_user=UserReg.objects.get(username=user)    ### object (users detail)


    print(user)
    print(cur_user)
    print(cur_user.f_name)


    if request.method == 'POST':

        form = eventregform()
        
        form = eventregmodel.objects.create(club = hack.club,fname = cur_user.f_name,lname = cur_user.l_name,usn = request.POST.get("company")
        , branch = request.POST.get("subject"),email = cur_user.email,event_title=eventtitle)
        return redirect("home")
    else:
        new_form=eventregform(initial= {'club':hack.club,'fname':cur_user.f_name,'lname':cur_user.l_name,'email':cur_user.email}  )
        return render(request,"hr_index.html",{'title':eventtitle,'form':new_form})







### login required ###








