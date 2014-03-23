from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from .models import *

class KeywordsResource(ModelResource):
    class Meta:
        queryset = Keywords.objects.all()
        resource_name = 'keywords'
        authorization=Authorization()

class BookResource(ModelResource):
    keywords = fields.ToManyField(KeywordsResource, 'keywords', blank=True, null=True)
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        authorization=Authorization()

