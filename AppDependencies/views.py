from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AppDependencies.models import HeroCard
from AppDependencies.serializer import HeroCardSerializer


class HeroCardLister(APIView):

    def get(self, request, format=None):
        database_objects = HeroCard.objects.all()
        serializer = HeroCardSerializer(database_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HeroCardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroCardDetail(APIView):

    def get_post(self, pk):
        try:
            return HeroCard.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = HeroCardSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = HeroCardSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

