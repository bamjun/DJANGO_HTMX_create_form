from django.shortcuts import redirect, render
from .models import Author, Book
from .forms import BookForm, BookFormSet

# Create your views here.


def first_views(request):
    return redirect('index', pk=1)


def index(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookFormSet(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance = author
            form.save()
            return redirect('index', pk=author.id)

    context = {
        "author": author,
        "form": form,
    }

    return render(request, "book/index.html", context)
