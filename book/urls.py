from django.urls import path
from . import views


app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('list/', views.BookListView.as_view(), name='BookList'),  # List of books
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='bookDetail'),  # Detail of a book
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='myBooks'),  # My books
    path('logged-out/', views.logged_out_view, name='logged-out'),  # Logged out page
    
]

