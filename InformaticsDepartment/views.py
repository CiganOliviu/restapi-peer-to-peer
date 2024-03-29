from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from InformaticsDepartment.serializers import *


class InformaticsGroupLister(APIView):

    def get(self, request, format=None):
        data_objects = InformaticsGroup.objects.all()
        serializer = InformaticsGroupSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InformaticsGroupSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformaticsGroupDetails(APIView):

    def get_post(self, pk):
        try:
            return InformaticsGroup.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsGroupSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsGroupSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class InformaticsScheduleLister(APIView):

    def get(self, request, format=None):
        data_objects = InformaticsSchedule.objects.all()
        serializer = InformaticsScheduleSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InformaticsScheduleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformaticsScheduleDetails(APIView):

    def get_post(self, pk):
        try:
            return InformaticsSchedule.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsScheduleSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsScheduleSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class InformaticsHomeworkLister(APIView):

    def get(self, request, format=None):
        data_objects = InformaticsHomework.objects.all()
        serializer = InformaticsHomeworkSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InformaticsHomeworkSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformaticsHomeworkDetails(APIView):

    def get_post(self, pk):
        try:
            return InformaticsHomework.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsHomeworkSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = InformaticsHomeworkSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
