from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from django.http import HttpResponse
from django.conf.urls import url

from models import Book
from book import create_book

class BookResource(ModelResource):

    class Meta:
        allowed_methods = ['get', 'post', 'put', 'delete']
        serializer = Serializer(formats=['json'])
        queryset = Book.objects.all()
        excludes = []

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        if data:
            return super(BookResource, self).create_response(request, data)
        else:
            return HttpResponse('Cannot process request')

    def dehydrate(self, bundle):
        if bundle.errors:
            return bundle.errors
        else:
            return bundle

    def prepend_urls(self):
        return [

            url(r"^(?P<resource_name>%s)/(?P<gid>[\w/-]*)/users%s$" %
                ('groups', trailing_slash())
                , self.wrap_view('handle_book')),
            ]

    def handle_book(self, request, **kwargs):
        kwargs['resource_name'] = 'users'
        return BookResource().dispatch(kwargs['req_type'], request, **kwargs)

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            create_book(kwargs)
            return HttpResponse('Book created successfully')
        except Exception as e:
            raise e