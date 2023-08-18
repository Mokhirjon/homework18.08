from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(default='',max_length=20)
    book_cost=models.IntegerField()
    book_year=models.DateField()

    def __str__(self):
        return self.book_name
class Avtors(models.Model):
    avtor_name=models.CharField(default='',max_length=23)
    avtor_bday=models.DateField()
    avtor_books_created_name=models.CharField(default='',max_length=23)
    avtor_date_of_die=models.DateField()
    Books_id=models.ForeignKey(Books,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.avtor_name