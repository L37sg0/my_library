from .views import bookAPIView
from django.conf.urls import url

app_name = 'books'
urlpatterns = [
    url(r'^$', bookAPIView.as_view(), name='book-create'),
]
