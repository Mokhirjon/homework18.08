from .serializers import AvtorsSerializer, BooksSerializer
from rest_framework.views import APIView
from .models import Books, Avtors
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import generics
#from .permissions import ReadonlyPeromissions
#from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BooklistALLView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


    # def get_queryset(self):
    #     user =self.request.user
    #     return Books.objects.filter(user=user)


class BookDetalesView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = (ReadonlyPeromissions)


class BookCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDeleteView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
