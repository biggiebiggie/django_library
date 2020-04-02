from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('loan_book/', views.loan_book, name="loan_book"),
    path('inventory/', views.inventory, name="inventory"),
    path('delete_book/', views.delete_book, name="delete_book"),
    path('add_book/', views.add_book, name="add_book"),
    path('return_book/', views.return_book, name="return_book"),
    path('loan_magazine/', views.loan_magazine, name="loan_magazine"),
    path('delete_magazine/', views.delete_magazine, name="delete_magazine"),
    path('add_magazine/', views.add_magazine, name="add_magazine"),
    path('return_magazine/', views.return_magazine, name="return_magazine"),
    path('list_of_checkouts/', views.list_of_checkouts, name="list_of_checkouts"),
]
