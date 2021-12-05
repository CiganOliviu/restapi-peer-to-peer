from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from MathematicsDepartment.models import (
    MathGroup,
    MathSchedule,
    MathHomework
)
from MathematicsDepartment.serializers import (
    MathematicsGroupSerializers,
    MathematicsScheduleSerializers,
    MathematicsHomeworkSerializers
)


class MathematicsGroupLister(APIView):

    def get(self, request, format=None):
        data_objects = MathGroup.objects.all()
        serializer = MathematicsGroupSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MathematicsGroupSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MathematicsGroupDetails(APIView):

    def get_post(self, pk):
        try:
            return MathGroup.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsGroupSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsGroupSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MathematicsScheduleLister(APIView):

    def get(self, request, format=None):
        data_locations = MathSchedule.objects.all()
        serializer = MathematicsScheduleSerializers(data_locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MathematicsScheduleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MathematicsScheduleDetails(APIView):

    def get_post(self, pk):
        try:
            return MathSchedule.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsScheduleSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsScheduleSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MathematicsHomeworkLister(APIView):

    def get(self, request, format=None):
        data_objects = MathHomework.objects.all()
        serializer = MathematicsHomeworkSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MathematicsHomeworkSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MathematicsHomeworkDetails(APIView):

    def get_post(self, pk):
        try:
            return MathHomework.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsHomeworkSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = MathematicsHomeworkSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
