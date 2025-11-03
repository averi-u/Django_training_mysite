from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from rest_framework .decorators import api.view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.core.cache import cache
from django.http import JsonResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def hello(request):
    return HttpResponse("Hello, world!")

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

def test_cache(request):
    cache.set("greeting", "hello", timeout=60)
    value = cache.get("greeting")
    return JsonResponse({"greeting": value})