from django.shortcuts import render
from BRMapp.forms import NewBookForm,SearchForm
from BRMapp import models
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.

def NewBook(request):
    form=NewBookForm()
    return render(request,'BRMapp/new_book.html',{'form':form})


def Add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Stored<br><a href='view-books'>View all Books</a>"
    return HttpResponse(s)

def viewBooks(request):
    books=models.Book.objects.all();
  # username=request.session['username']
    return render(request,'BRMapp/view_book.html',{'books':books})

def editbook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    return render(request,'BRMapp/edit_book.html',{'form':form,'book':book})

def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('view-books')

def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('view-books')

def searchBook(request):
    form=SearchForm()
    return render(request,'BRMapp/search_book.html',{'form':form})

def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    return render(request,'BRMapp/search_book.html',{'form':form,'books':books})

