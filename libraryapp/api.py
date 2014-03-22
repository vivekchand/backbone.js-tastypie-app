from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from .models import *

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'


