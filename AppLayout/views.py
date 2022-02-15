from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AppLayout.models import HeroCard, HomeworkCard, ScheduleCard
from AppLayout.serializer import HeroCardSerializer, HomeworkCardSerializer, ScheduleCardSerializer


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


class HomeworkCardLister(APIView):

    def get(self, request, format=None):
        database_objects = HomeworkCard.objects.all()
        serializer = HomeworkCardSerializer(database_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HomeworkCardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeworkCardDetail(APIView):

    def get_post(self, pk):
        try:
            return HomeworkCard.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = HomeworkCardSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = HomeworkCardSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ScheduleCardLister(APIView):

    def get(self, request, format=None):
        database_objects = ScheduleCard.objects.all()
        serializer = ScheduleCardSerializer(database_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleCardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleCardDetail(APIView):

    def get_post(self, pk):
        try:
            return ScheduleCard.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ScheduleCardSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ScheduleCardSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
