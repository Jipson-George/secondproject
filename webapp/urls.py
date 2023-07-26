from django.urls import path
from webapp import views

urlpatterns = [
    path('webpage/',views.webpage,name="webpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('showproduct/<cat_name>',views.showproduct,name="showproduct"),
    path('sproduct/<int:proid>/',views.sproduct,name="sproduct"),
    path('regpage/',views.regpage,name="regpage"),
    path('signpage/',views.signpage,name="signpage"),
    path('savereg/',views.savereg,name="savereg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('addcart/',views.addcart,name="addcart"),
    path('delitem/<int:cartid>/',views.delitem,name="delitem"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('savebill/',views.savebill,name="savebill")


]
