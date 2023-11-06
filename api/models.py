from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class LibUser(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    returnedDate = models.DateTimeField(null=True, blank=True)

    def str(self):
        return self.rentDate
