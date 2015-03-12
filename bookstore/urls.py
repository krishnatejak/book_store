from django.conf.urls import patterns, include, url
from django.contrib import admin

from store.handler import BookResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'book/?<book_id>[\w+]/?', BookResource())
)
