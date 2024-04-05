import datetime
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Book, BookInstance, Author, Genre


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import logout


def email_check(user):
    return user.email.endswith('@example.com')




@login_required
@permission_required('book.can_read_private_section')
@permission_required('book.user_watcher')
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_author,
    }

    return render(request, 'book/index.html', context)


class BookListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 5
    permission_required = 'book.can_read_private_section'
    permission_required = 'book.user_watcher'
    permission_required = 'user.can_edit'

    def test_func(self):
        return self.request.user.email.endswith('@example.com')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book


def logged_out_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'book/bookinstance_list_borrower_user.html'
    paginate_by = 5



    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user, status__exact='o').order_by('due_back')
    

    

    
    

    
      


    
    
    
    

    


    



