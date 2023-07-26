from django.shortcuts import render,redirect
from Backend.models import catagorydb,productdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
def adminpage(request):

    return render(request,"adminhome.html")
def categorypage(req):
    return render(req,"addcatagory.html")
def displaycategory(req):
    cat = catagorydb.objects.all()

    return render(req,"displaycategory.html",{'cat':cat})
def editcat (req,catid):
    cat = catagorydb.objects.get(id=catid)
    messages.success(req, "category edited successfully")
    return render(req,"editcategory.html",{'cat':cat})

def savecat(req,catid):
    if req.method =="POST":
        na = req.POST.get('Name')
        de = req.POST.get('Description')
        try:
            img = req.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catagorydb.objects.get(id=catid).cimage
        catagorydb.objects.filter(id=catid).update(cname=na,cdes=de,cimage=file)
        messages.success(req, "category edited successfully")
        return redirect(displaycategory)
def deletecat(req,catid):
    data = catagorydb.objects.get(id=catid)
    data.delete()
    messages.success(req, "category deleted successfully")

    return redirect(displaycategory)
def savecatagory(req):
    if req.method =="POST":
        cn = req.POST.get('Name')
        cd = req.POST.get('Description')
        cimg = req.FILES['Image']
        obj=catagorydb(cname=cn,cdes=cd,cimage=cimg)
        obj.save()
        messages.success(req, "category saved successfully")
        return redirect(categorypage)

def productpage(req):
    cat = catagorydb.objects.all()
    return render(req,"addproduct.html",{'cat':cat})
def saveproduct(req):
    if req.method =="POST":
        ps = req.POST.get('Select')
        pn = req.POST.get('Name')
        pd = req.POST.get('Description')
        pp = req.POST.get('Price')
        pimg = req.FILES['Image']
        obj = productdb(pselect=ps,pname=pn,pdes=pd,pprice=pp,pimage=pimg)
        obj.save()
        messages.success(req, "product saved successfully")
        return redirect(productpage)
def productdisplay(req):
    pdata= productdb.objects.all()
    return render(req,"displayproduct.html",{'pdata':pdata})
def productedit(req,pid):
    cat = catagorydb.objects.all()
    pdata = productdb.objects.get(id=pid)
    return render(req,"editproduct.html",{'cat':cat,'pdata':pdata})
def updateproduct(req,pid):
    if req.method=="POST":
        Ps = req.POST.get('Select')
        Pn = req.POST.get('Name')
        Pd = req.POST.get('Description')
        Pp = req.POST.get('Price')
        try:
            Pimg = req.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(Pimg.name,Pimg)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pid).pimage
        productdb.objects.filter(id=pid).update(pselect=Ps,pname=Pn,pdes=Pd,pprice=Pp,pimage=file)
        messages.success(req, "updated successfully")
        return redirect(productdisplay)

def deleteproduct(req,pid):
    pdata = productdb.objects.get(id=pid)
    pdata.delete()
    return redirect(productdisplay)
def adminlogin(request):
    return render(request,"adminlogin.html")
def loginpage(request):
    if request.method =="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request, "login successfull")
                return redirect(adminpage)
            else:
                messages.error(request, "invalid username or password")
                return redirect(adminlogin)
        else:
            messages.error(request, "invalid username or password")
            return redirect(adminlogin)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)
