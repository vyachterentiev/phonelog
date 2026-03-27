from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class ContactType(models.Model):
    name = models.CharField(max_length=200)
    sort = models.CharField(max_length=200)

class Contacts(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)



