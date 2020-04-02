from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Book, Magazine


# Create your views here.


def index(request):
    books = Book.objects.filter(status=False)
    book_count = Book.objects.filter(status=False).count()
    magazines = Magazine.objects.filter(status=False)
    magazine_count = Magazine.objects.filter(status=False).count()
    context = {
        'books': books,
        'magazines': magazines,
        'book_counter': book_count,
        'magazine_counter': magazine_count
    }

    return render(request, 'library_app/index.html', context)

@login_required
def inventory(request):
    books = Book.objects.filter(user=request.user, status=True)
    book_count = Book.objects.filter(user=request.user, status=True).count()
    magazines = Magazine.objects.filter(user=request.user, status=True)
    magazine_count = Magazine.objects.filter(user=request.user, status=True).count()

    context = {
        'books': books,
        'magazines': magazines,
        'book_counter': book_count,
        'magazine_counter': magazine_count
    }
    return render(request, 'library_app/inventory.html', context)

@staff_member_required
def list_of_checkouts(request):
    date_30_days = datetime.now() + timedelta(days=30)
    books = Book.objects.filter(loan_date__gt=date_30_days)
    date_7_days = datetime.now() + timedelta(days=7)
    magazines = Magazine.objects.filter(loan_date__gt=date_7_days)
    context = {
        'books': books,
        'magazines': magazines
    }
    return render(request, 'library_app/list_of_checkouts.html', context)

@login_required
def loan_book(request):
    amount_of_books = Book.objects.filter(user=request.user).count()
    if amount_of_books < 10:
        pk = request.POST["pk"]
        book = get_object_or_404(Book, pk=pk)
        book.status = True
        book.user = request.user
        book.loan_date = datetime.now()
        print(book.user, book.loan_date)
        book.save()
        return HttpResponseRedirect(reverse('library_app:inventory'))
    else:
        books = Book.objects.filter(status=False)
        book_count = Book.objects.filter(status=False).count()
        magazines = Magazine.objects.all()
        context = {
            'error': 'No more than 10 books, please return some books',
            'books': books,
            'magazines': magazines,
            'book_counter': book_count
        }
    return render(request, 'library_app/index.html', context)

@login_required
def loan_magazine(request):
    amount_of_magazines = Magazine.objects.filter(user=request.user).count()
    if amount_of_magazines < 7:
        pk = request.POST["pk"]
        magazine = get_object_or_404(Magazine, pk=pk)
        magazine.status = True
        magazine.user = request.user
        magazine.loan_date = datetime.now()
        print(magazine.user, magazine.loan_date)
        magazine.save()
        return HttpResponseRedirect(reverse('library_app:inventory'))
    else:
        magazines = Magazine.objects.filter(status=False)
        magazine_count = Magazine.objects.filter(status=False).count()
        books = Book.objects.all()
        context = {
            'error': 'No more than 7 magazines, please return some magazines',
            'magazines': magazines,
            'books': books,
            'magazine_counter': magazine_count
        }
    return render(request, 'library_app/index.html', context)

@login_required
def return_book(request):
    pk = request.POST["pk"]
    book = get_object_or_404(Book, pk=pk)
    book.status = False
    book.loan_date = None
    book.user = None
    print(book.loan_date, book.user)
    book.save()
    return HttpResponseRedirect(reverse('library_app:inventory'))

@login_required
def return_magazine(request):
    pk = request.POST["pk"]
    magazine = get_object_or_404(Magazine, pk=pk)
    magazine.status = False
    magazine.loan_date = None
    magazine.user = None
    print(magazine.loan_date, magazine.user)
    magazine.save()
    return HttpResponseRedirect(reverse('library_app:inventory'))

@staff_member_required
def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        description = request.POST["description"]
        book = Book()
        book.title = title
        book.author = author
        book.description = description
        print(book.user, book.loan_date)
        book.save()
        return HttpResponseRedirect(reverse('library_app:index'))
    return render(request, 'library_app/add_book.html')

@staff_member_required
def add_magazine(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        magazine = Magazine()
        magazine.title = title
        magazine.description = description
        print(magazine.user, magazine.loan_date)
        magazine.save()
        return HttpResponseRedirect(reverse('library_app:index'))
    return render(request, 'library_app/add_magazine.html')

@staff_member_required
def delete_book(request):
    pk = request.POST["pk"]
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('library_app:index'))

@staff_member_required
def delete_magazine(request):
    pk = request.POST["pk"]
    magazine = get_object_or_404(Magazine, pk=pk)
    magazine.delete()
    return HttpResponseRedirect(reverse('library_app:index'))
