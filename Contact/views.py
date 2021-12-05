from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Contact.serializers import ContactSerializers
from Contact.models import Contact


class ContactLister(APIView):

    def get(self, request, format=None):
        data_objects = Contact.objects.all()
        serializer = ContactSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):

    def get_post(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ContactSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ContactSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
