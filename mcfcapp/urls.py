
from mcfcapp.views import *
from django.urls import include, path
from mcfcapp import views
from django.conf import settings

app_name = "mcfcapp"
urlpatterns = [
    path('', ClientHomeView.as_view(), name='clienthome'),
    path('member/', ClientMemberView.as_view(), name='clientmember'),
    path('event/', ClientEventView.as_view(), name='clientevent'),
    path('gallery/', ClientGalleryView.as_view(), name='clientgallery'),

]
