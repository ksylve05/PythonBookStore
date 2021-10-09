from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import Book
from .models import OrderItem
from .models import OrderDetail


# Create your views here.
def cart(request):
    user = request.user.id
    orders = OrderItem.objects.filter(userId = user)
    total = 0
    for x in orders:
        total += x.quanity * x.price

    return render(request, 'accounts/cart.html', {'orders': orders, 'total':total})


def orders(request):
    user = request.user.id
    orders = OrderDetail.objects.filter(userId = user)
    
    return render(request, 'accounts/orders.html', {'orders': orders})


def addOrderedItems(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        price = request.POST.get("price")
        image = request.POST.get("image")
        title = request.POST.get("title")
        quanity = request.POST.get("quanity")

        newOrder = OrderDetail.objects.create(userId=userId, price=price, image=image, title=title, quanity=quanity)
        newOrder.save()
        
    return redirect('/account/orders')


def addOrder(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        price = request.POST.get("price")
        image = request.POST.get("image")
        title = request.POST.get("title")

        newOrder = OrderItem.objects.create(userId=userId, price=price, image=image, title=title)
        newOrder.save()
        
    return redirect('/account/')


def deleteOrder(request):
    if request.method == "POST":
        delete = request.POST.get("delete")
        OrderItem.objects.filter(id=delete).delete()
   
    return redirect('/account/cart')


def updateOrder(request):
    if request.method == "POST":
        update = request.POST.get("update")
        quanity = request.POST.get("quanity")
        OrderItem.objects.filter(id=update).update(quanity=quanity)
   
    return redirect('/account/cart')


def home(request):
    books = Book.objects.all()
    return render(request, 'accounts/home.html', {'user': request.user, 'book': books})

def admin(request):
    books = Book.objects.all()
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'accounts/admin.html', {'user': request.user, 'book': books, 'users': users})


def addBook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        quanity = request.POST.get("quanity")
        image = request.POST.get("image")
        newBook = Book.objects.create(title=title, author=author, price=price, quanity=quanity, image=image)
        newBook.save()
        
    return redirect('/account/admin')


def deleteBook(request):
    if request.method == "POST":
        delete = request.POST.get("delete")
        Book.objects.filter(id=delete).delete()
   
    return redirect('/account/admin')


def editBook(request):
    if request.method == "POST":
        edit = request.POST.get("edit")
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        quanity = request.POST.get("quanity")
        image = request.POST.get("image")
        Book.objects.filter(id = edit).update(title=title, author=author, price=price, quanity=quanity, image=image)
   
    return redirect('/account/admin')


def addUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        User = get_user_model()
        newUser = User.objects.create(username=username)
        newUser.save()
        
    return redirect('/account/admin')


def deleteUser(request):
    if request.method == "POST":
        delete = request.POST.get("delete")
        User = get_user_model()
        User.objects.filter(id=delete).delete()
   
    return redirect('/account/admin')


def editUser(request):
    if request.method == "POST":
        edit = request.POST.get("edit")
        username = request.POST.get("username")
        User = get_user_model()
        User.objects.filter(id = edit).update(username=username)
   
    return redirect('/account/admin')


def search(request):
    if request.method == "POST":
        title = request.POST.get("q")
        books = Book.objects.filter(title__contains=title)
    else:
        books = Book.objects.all()  
   
    return render(request, 'accounts/search.html', {'user': request.user, 'book': books})


def logout(request):
    logout(request)
    return redirect('/account')
    


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
