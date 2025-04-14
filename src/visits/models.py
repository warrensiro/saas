from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db table
    # id -> col of primary key(auto field whcih increments linearly)
    path = models.TextField(blank=True, null=True) # col
    # timestamp = models.DateTimeField(auto_now_add=True) # col 