from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *


class ClientHomeView(TemplateView):
    template_name = 'clienttemplates/clienthomepage.html'


class ClientMemberView(TemplateView):
    template_name = 'clienttemplates/clientmemberpage.html'


class ClientEventView(TemplateView):
    template_name = 'clienttemplates/clienteventpage.html'


class ClientGalleryView(TemplateView):
    template_name = 'clienttemplates/clientgallerypage.html'
