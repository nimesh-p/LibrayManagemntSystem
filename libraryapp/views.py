from libraryapp.serializers import RegistrationSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_auth.serializers import LoginSerializer
from rest_framework import permissions
from django.contrib.auth import login
from rest_framework.views import APIView
from libraryapp.models import Book
from rest_framework.permissions import IsAuthenticated


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message": "Admin Signup Successfully....",
                    "User": serializer.data,
                    "Status": status.HTTP_201_CREATED,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(
            {
                "Message": "Login Successfully....",
                "Status": status.HTTP_201_CREATED,
            }
        )


class ListBook(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk=None):
        return Book.objects.get(pk=pk)

    def get(self, request, pk=None):
        if pk:
            snippet = Book.objects.get(id=pk)
            serializer = BookSerializer(snippet)
        else:
            snippet = Book.objects.all()
            serializer = BookSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message": "Data Created Successfully....",
                    "User": serializer.data,
                    "Status": status.HTTP_201_CREATED,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        snippet = self.get_object(pk)
        serializer = BookSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message": "Data Updated Successfully....",
                    "User": serializer.data,
                    "Status": status.HTTP_201_CREATED,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        snippet = self.get_object(pk)
        serializer = BookSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message": "Data Updated Successfully....",
                    "User": serializer.data,
                    "Status": status.HTTP_201_CREATED,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(
            {
                "Message": "Data Deleted Successfully....",
                "Status": status.HTTP_204_NO_CONTENT,
            }
        )


"""This is second way that i created api using generics """


class ListBookApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBookApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
