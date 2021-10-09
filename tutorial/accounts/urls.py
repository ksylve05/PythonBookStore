from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('admin/', views.admin, name="admin"),
    path('cart/', views.cart, name="cart"),
    path('orders/', views.orders, name="orders"),
    path('addBook/', views.addBook, name="addBook"),
    path('deleteBook/', views.deleteBook, name="deleteBook"),
    path('editBook/', views.editBook, name="editBook"),
    path('addUser/', views.addUser, name="addUser"),
    path('deleteUser/', views.deleteUser, name="deleteUser"),
    path('editUser/', views.editUser, name="editUser"),
    path('addOrder/', views.addOrder, name="addOrder"),
    path('deleteOrder/', views.deleteOrder, name="deleteOrder"),
    path('updateOrder/', views.updateOrder, name="updateOrder"),
    path('addOrderedItems/', views.addOrderedItems, name="addOrderedItems"),
]
