import imp
from django.urls import  path
from core.views import BooksListView, DeleteAllBooks, home, start_scraping_books, toExcel


urlpatterns = [
    path('', home, name="books-home"),
    path('excel/', toExcel, name="excel"),
    path('books/', BooksListView.as_view(),name='books-list'),
    path('delete-books/', DeleteAllBooks,name='delete-books'),
    path('start-scraping-books/', start_scraping_books,name='start-scraping-books'),
]
