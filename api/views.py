from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])
def get_user(request):
    user = User(email="contact.mdemonmiah@gmail.com", name="Emon", age=22)
    serializer = UserSerializer(user)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"error": "Invalid method"}, status=405) 