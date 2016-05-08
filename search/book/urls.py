from django.conf.urls import url

from .import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/(?P<ebook_id>[0-9]+)/$', views.books, name='books'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^register/', views.register, name='register'),
	url(r'^changefile/', views.changefile, name='changefile'),
]
