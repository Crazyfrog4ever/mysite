from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Genre(models.Model) :
    name = models.CharField(max_length = 200 , help_text = 'Enter A Book Genre(e.g. Science Fiction, French Poetry etc.)')

    def __str__(self) :
        return self.name
    

class Book (models.Model) :
    title = models.CharField(max_length = 200)
    summary = models.TextField(max_length = 1000 , help_text = 'Enter A Brief Description Of The Book')  
    isbn = models.CharField(max_length = 13 , help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISNB number</a>')
    genre = models.ManyToManyField(Genre, help_text = 'Select A Genre For This Book')
    author = models.ForeignKey('Author' , on_delete = models.SET_NULL , null = True)

    def __str__(self) :
        return self.title


class Author (models.Model) :
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True , blank = True)
    date_of_death = models.DateField('Died' , null = True , blank = True)

    class Meta :
        ordering = ["-last_name" , "first_name"]

    def __str__(self) :
        return '{0} , {1}'.format(self.last_name , self.first_name)
    

class BookInstance(models.Model) :
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 ,
                          help_text = 'Unique ID For This Particular Book Across Whole Library')
    book = models.ForeignKey('Book' , on_delete = models.SET_NULL , null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True , blank = True)
    borrower = models.ForeignKey(User , on_delete = models.SET_NULL , null= True , blank = True)


    LOAN_STATUS = (
        ('m' , 'Maintenance'),
        ('o' , 'On Loan'),
        ('a' , 'Available'),
        ('r' , 'Reserved'),

    )

    status = models.CharField(max_length = 1 , 
                              choices = LOAN_STATUS,
                              blank = True,
                              default = 'm',
                              help_text = 'Book Availability')
    
    class Meta :
        ordering = ["due_back"]
        permissions = (
            ("can_read_private_section" , "VIP User"),
            ("user_watcher" , "User_watcher"),
            

        )


    @property
    def is_overdue(self) :
        if self.due_back and date.today() > self.due_back :
            return True 
        return False    


    def __str__(self) :
        return '{0} ({1})'.format(self.id , self.book.title)    





