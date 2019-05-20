from django.shortcuts import render, HttpResponse, redirect
from apps.books_authors_app.models import *
from django.contrib.sessions.models import Session

def index(request):
    context = {"books": Book.objects.all()}
    # print('*' * 80)
    # print(context)
    return render(request, "books_authors_app/index.html", context)

def books(request, num):
    id = int(num)
    request.session['id'] = id
    context = {
        "books": Book.objects.get(id=id),
        "authors": Author.objects.all()
    }
    print('*' * 80)
    print(context)
    print(request.session['id'])
    return render(request, "books_authors_app/showbooks.html", context)

def add_book(request):
    if request.method == "POST":
        book = Book.objects.create(title=request.POST['title'], description=request.POST['description'])
        print(book)
        print('*' * 80)
    if request.method == "GET":
        print('yooo its a get')
    return redirect('/', book)

def add_auth_to_book(request):
    if request.method == "POST":
        print(request.POST["id"])
        print('*' * 80)
        id = request.session['id']
        auth_id = request.POST["id"]
        print(id)
        context = {
        "books": Book.objects.get(id=id),
        "authors": Author.objects.all()
        }
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=auth_id)
        print(author.id)
        book.author.add(author)
    return redirect('/')

def authors(request):
    context = {"authors": Author.objects.all()}
    # print('*' * 80)
    # print(context)
    return render(request, "books_authors_app/authors.html", context)

def addauthor(request):
    if request.method == "POST":
        author = Author.objects.create(first_name=request.POST['fn'], last_name=request.POST['ln'], notes=request.POST['notes'])
        print(author)
        print('*' * 80)
    if request.method == "GET":
        print('yooo its a get')
    return redirect('/authors', author)

def showauthors(request, num):
    id = int(num)
    request.session['ida'] = id
    # print(request.session['ida'])
    context = {
        "authors": Author.objects.get(id=id),
        "books": Book.objects.all()
        }
    # print('*' * 80)
    # print(context)
    return render(request, "books_authors_app/showauthors.html", context)

def add_book_to_auth(request):
    if request.method == "POST":
        print(request.POST["ida"])
        print('*' * 80)
        id = request.session['ida']
        book_id = request.POST["ida"]
        print(id)
        print(book_id)
        context = {
        "authors": Author.objects.get(id=id),
        "books": Book.objects.all()
        }
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=book_id)
        print(book.id)
        author.books.add(book)
    return redirect('/authors')