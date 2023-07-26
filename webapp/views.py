from django.shortcuts import render,redirect
from Backend.models import catagorydb,productdb
from webapp.models import regdb,cartdb,billdb
from django.contrib import messages
# Create your views here.
def webpage(request):
    data = catagorydb.objects.all()
    return render(request,"webiste.html",{'data':data})
def aboutpage(req):
    data = catagorydb.objects.all()
    return render(req,"aboutus.html",{'data':data})
def contactpage(req):
    data = catagorydb.objects.all()
    return render(req,"contactus.html",{'data':data})
def showproduct(req,cat_name):
    cat = catagorydb.objects.all()
    pro = productdb.objects.filter(pselect=cat_name)
    return render(req,"products.html",{'pro':pro,'cat':cat})
def sproduct(request,proid):
    cat = catagorydb.objects.all()
    pdata = productdb.objects.get(id=proid)
    return render(request,"singleproduct.html",{'pdata':pdata,'cat':cat})
def regpage(req):
    return render(req,"reg.html")
def signpage(req):
    return render(req,"signin.html")
def savereg(req):
    if req.method =="POST":
        rn = req.POST.get('Username')
        re = req.POST.get('Email')
        rm = req.POST.get('Mobile')
        rp = req.POST.get('Password')
        rimg = req.FILES['Image']
        obj = regdb(rname=rn,remail=re,rmobile=rm,rpas=rp,rimage=rimg)
        obj.save()
        return redirect(regpage)
def userlogin(request):
    if request.method =="POST":
        uname = request.POST.get("Username")
        pwd = request.POST.get("Password")
        if regdb.objects.filter(rname=uname,rpas=pwd).exists():
            request.session['Username']=uname
            request.session['Password']=pwd
            return redirect(webpage)
        else:
            return redirect(regpage)
    return redirect(regpage)
def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(signpage)
def cartpage(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pname = request.POST.get('product')
        cdes = request.POST.get('description')
        qu = request.POST.get('quantity')
        tp = request.POST.get('totalprice')
        obj = cartdb(username=uname,productname=pname,description=cdes,quantity=qu,totalprice=tp)
        obj.save()
        messages.success(request, "item added to cart ")
        return redirect(addcart)
def addcart(request):
    cdata =cartdb.objects.filter(username=request.session['Username'])
    total_price = 0
    for i in cdata :
        total_price = total_price+i.totalprice
    return render(request,"cart.html",{'cdata':cdata,'total_price':total_price})

def delitem(req,cartid):
    cdata = cartdb.objects.filter(id=cartid)
    cdata.delete()
    return redirect(addcart)
def checkoutpage(request):
    cdata = cartdb.objects.filter(username=request.session['Username'])
    total_price = 0
    for i in cdata:
        total_price = total_price + i.totalprice
    return render(request,"checkout.html",{'cdata':cdata,'total_price':total_price})
def savebill(request):
    if request.method =="POST":
        na = request.POST.get('User')
        em = request.POST.get('Email')
        ad = request.POST.get('Address')
        mo = request.POST.get('Mobile')
        obj = billdb(name=na,email=em,address=ad,mobile=mo)
        obj.save()
        messages.success(request, "Order placed successfully ")
        return redirect(checkoutpage)