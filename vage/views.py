# from django.shortcuts import render

# # Create your views here.
# '''def receipes(request):
#     if request.method=="POST":
#         data=request.POST
#         name=data.get("name")
#         description=data.get("description")
#         image=request.FILES.get("image")

#         print(name)
#         print(description)
#         print(image)
#     return render(request,'receipes.html')'''


# def receipes(request):
#     if request.method=="POST":
#         data=request.POST
#         name=data.get("name")
#         description=data.get("description")
#         image=request.FILES.get("image")

#         print(name)
#         print(description)
#         print(image)

#         receipes.objects.create(
#             name=name,
#             description=description,
#             image=image
#         )
#         queryset=receipes.objects.all()
#         context={'receipes':queryset}
#         return render(request,'receipes.html',context)


from django.shortcuts import redirect, render
from vage.models import*  # Ensure your model is imported

def receipes(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        description = data.get("description")
        image = request.FILES.get("image")

        print(name)
        print(description)
        print(image)

        Receipe.objects.create(
            name=name,
            description=description,
            image=image
        )

    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete(request,id):
    queryset=Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def update(request,id):
    queryset=Receipe.objects.get(id = id)

    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        description=data.get("description")
        image=request.FILES.get("image")

        queryset.name=name
        queryset.description=description

        if image:
            queryset.image=image
        queryset.save()
        return redirect('/receipes/')
    
    context={'receipes':queryset}
    return render(request, 'update.html', context)



# from django.contrib.auth.models import User
# def register(request):
#     if request.method == "POST":
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         if first_name and last_name and username and password:
#             user=User.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 password=password
#             )
#             user.set_password(password)
#             user.save()

#             return redirect('/register/')
        
#         else:
#             context = {"error":"all fields are required"}
#             return render(request,'register.html',context)
#     return render(request,'register.html')

from django.contrib.auth.models import User
def register(request): 
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if first_name and last_name and username and password:
            user=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )
            user.set_password(password)
            user.save()

            return redirect('/register/')
        
        else:
            context = {"error":"all fields are required"}
            return render(request,'register.html',context)
    return render(request,'register.html')




def form(request):
        return render(request,"form.html")

from django.contrib import admin
from .models import tcp

admin.site.register(tcp)


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        tcp.objects.create(name=name, email=email, contact=contact, message=message)
        return redirect('form')

    return render(request, "form.html")


from django.contrib.auth.hashers import check_password
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password,user.password)
            if pwd:
                return redirect('/receipes/')
            else:
                return render(request,'login.html',{'errormsg':'invalid password'})
        else:
            return render(request,'login.html',{'errormsg':'Invalid Login'})
    return render(request,'login.html')


def task(request):
    return render(request,'task.html')

def demo(request):
    return render(request,'demo.html')
    
def about(request):
    return render(request,'about.html')





# def RAGISTER(request): 
#     if request.method == "POST":
#         usrname=request.POST.get('usrname')
#         usremaile=request.POST.get('usremaile')
#         usrcontact=request.POST.get('usrcontact')
#         urspassword=request.POST.get('urspassword')
#         ursstates=request.POST.get('ursstates')``

#         if usrname and usremaile and usrcontact and urspassword and ursstates:
#             user=userroy.objects.create(
#                 usrname=usrname,
#                 usremaile=usremaile,
#                 usrcontact= usrcontact,
#                 urspassword=urspassword,
#                 ursstates=True,
#             )
#             user.save()

#             return redirect('/RAGISTER/')
        
#         else:
#             context = {"error":"all fields are required"}
#             return render(request,'RAGISTER.html',context)
#     return render(request,'RAGISTER.html')

def RAGISTER(request): 
    if request.method == "POST":
        usrname = request.POST.get('usrname')
        usrEmail = request.POST.get('usrEmail')
        usrcontect = request.POST.get('usrcontact')
        usrpassword = request.POST.get('usrpassword')
        usrstates = request.POST.get('usrstates')

        if usrname and usrEmail and  usrcontect  and  usrpassword and  usrstates:
            user = userroy.objects.create(
                usrname=usrname,
                 usrEmail= usrEmail,
                 usrcontect=int( usrcontect),
                  usrpassword =  usrpassword ,
                usrstates=True if  usrstates.lower() == 'true' else False
            )
            user.save()
            return redirect('/RAGISTER/')
        else:
            context = {"error": "All fields are required"}
            return render(request, 'RAGISTER.html', context)
    return render(request, 'RAGISTER.html')


def hed(request):
    if request.method == "POST":
        usrname = request.POST.get('usrname')
        usrpassword = request.POST.get("usrpassword")

        user = userroy.objects.filter(usrname=usrname).first()
        if user:
            if usrpassword == user.usrpassword:  # use check_password if hashed
                return redirect('/RAGISTER/')
            else:
                return render(request,'hed.html',{'errormsg':'invalid password'})
        else:
            return render(request,'hed.html',{'errormsg':'Invalid Login'})
    return render(request,'hed.html')




def shreya(request):
    return render(request,'shreya.html')

def ptns(request):
    queryset = ptnsmasten.objects.all()    
    return render(request,'ptns.html',{'datatable':queryset})

def loginptn(request):
    return render(request,'data.html')


def loginptn(request):
    if request.method == 'POST':
        pasname = request.POST.get('pasname')
        pascontact = request.POST.get('pascontact')
        pasaddress = request.POST.get('pasaddress')
        pascity = request.POST.get('pascity')
        pasStatus = request.POST.get('pasStatus') == 'on'

        ptn = ptnsmasten.objects.create(
            pasname = pasname,
            pascontact = pascontact,
            pasaddress = pasaddress,
            pascity = pascity,
            pasStatus = pasStatus
        )
        ptn.save()
        return redirect('/ptns')

    return render(request, 'data.html')


def delete_pts(request, id):
    queryset = ptnsmasten.objects.get(id = id)
    queryset.delete()
    return redirect('/ptns')


#task session

def session(request):
    request.session['username']='Mansi'
    return render(request,'session.html')

def get(request):
    if request.session.get('user'):
        return render(request,'get.html')
    else:
        return redirect('/loginfrm')

def logout(request):
    request.session.flush()
    return redirect('/loginfrm')

#session (save data code)

def loginhp(request):
    if request.method == 'POST':
        Usrname = request.POST.get('Usrname')
        UsrEmaile= request.POST.get('UsrEmaile')
        UsrPassword = request.POST.get('UsrPassword')
        
        ptns = userps.objects.create(
            Usrname= Usrname,
            UsrEmaile = UsrEmaile,
            UsrPassword = UsrPassword
        )
        ptns.save()
        return redirect('/loginfrm')

    return render(request, 'mansi.html')


def loginfrm(request):
    if request.session.get('user'):
        return redirect('/get')
    if request.method == "POST":
        Usrname=request.POST.get('Usrname')
        UsrPassword=request.POST.get('UsrPassword')

        user = userps.objects.filter(Usrname=Usrname).first()
        if user:
            request.session['user']=Usrname
        else:
            return render(request,'mansi.html',{'errormsg':'Invalid Login'})
        
    return render (request,'loginweb.html')