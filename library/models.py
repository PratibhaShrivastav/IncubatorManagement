from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    BOOK_TYPE = (
        ('MGZ','MAGAZINE'),
        ('RSP','RESEARCH PAPER'),
        ('EBK','EBOOK'),
        ('OTH','OTHER')
    )

    GENRE = (
        ('TECH','TECHNOLOGY'),
        ('SCIN','SCIENCE'),
        ('FICT','FICTION'),
        ('REFR','REFERENCE'),
    )

    title = models.CharField(max_length = 150)
    book_type = models.CharField(max_length=3,choices = BOOK_TYPE)
    genre = models.CharField(max_length=4,choices = GENRE)
    isbn = models.CharField(max_length = 100)
    description = models.TextField()
    author = models.CharField(max_length = 50)
    is_issued = models.BooleanField(default = True)

    def __str__(self):
        return self.title

class BookLog(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    issue_start_dt = models.DateTimeField()
    issue_end_dt = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.book.title + ' issued by -> ' + self.user.username

