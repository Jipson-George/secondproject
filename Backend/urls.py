from django.urls import path
from Backend import views

urlpatterns = [
    path('adminpage/',views.adminpage,name="adminpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savecatagory/',views.savecatagory,name="savecatagory"),
    path('productpage/',views.productpage,name="productpage"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcat/<int:catid>/',views.editcat,name="editcat"),
    path('savecat/<int:catid>/',views.savecat,name="savecat"),
    path('deletecat/<int:catid>/',views.deletecat,name="deletecat"),
    path('productdisplay/',views.productdisplay,name="productdisplay"),
    path('productedit/<int:pid>/',views.productedit,name="productedit"),
    path('updateproduct/<int:pid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:pid>/',views.deleteproduct,name="deleteproduct")
]