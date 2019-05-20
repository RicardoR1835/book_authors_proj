from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<num>\d+)$', views.books),
    url(r'^books/add_auth_to_book$', views.add_auth_to_book),
    url(r'^authors$', views.authors),
    url(r'^addauthor$', views.addauthor),
    url(r'^authors/(?P<num>\d+)$', views.showauthors),
    url(r'^authors/add_book_to_auth$', views.add_book_to_auth),
]
