from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Author, Book
from .forms import BookForm, BookFormSet

# Create your views here.


def first_views(request):
    return redirect('index', pk=1)


def index(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect('detail-form', pk=book.id)
        else:
            context = {
                "form": form,
            }
            return render(request, "partials/create_form.html", context)

    context = {
        "author": author,
        "form": form,
        "books": books,
    }

    return render(request, "book/index.html", context)


def create_form(request):
    context = {
        "form": BookForm()
    }
    return render(request, "partials/create_form.html", context)


def detail_form(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, "partials/detail_form.html", context)


def update_form(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect('detail-form', pk=book.id)

    context = {
        "form": form,
        "book": book
    }
    return render(request, "partials/create_form.html", context)


def delete_form(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse("")
