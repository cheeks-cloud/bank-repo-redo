from .models import *
from .serializers import *
from rest_framework import viewsets
from .forms import *
from django.urls import include, re_path
from django.shortcuts import render,redirect

def home(request):
    members = Member.objects.all()
    return render( request, "home.html", {'members': members})



class MembersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class AccountsViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = memberAccounts.objects.all()
    serializer_class = AccountsSerializer

    def perform_create(self, serializer):
        serializer.save()



class CardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = membercardnum.objects.all()
    serializer_class = CardsSerializer

    def perform_create(self, serializer):
        serializer.save()


