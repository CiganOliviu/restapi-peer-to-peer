from django.http import Http404

from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class MathematicsGroupLister(APIView):

    def get(self, request, format=None):
        locations = MathGroup.objects.all()
        serializer = MathematicsGroupSerializers(locations, many=True)

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
        locations = self.get_post(pk)
        serializer = MathematicsGroupSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MathematicsScheduleLister(APIView):

    def get(self, request, format=None):
        locations = MathSchedule.objects.all()
        serializer = MathematicsScheduleSerializers(locations, many=True)

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
        locations = self.get_post(pk)
        serializer = MathematicsScheduleSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MathematicsHomeworkLister(APIView):

    def get(self, request, format=None):
        locations = MathHomework.objects.all()
        serializer = MathematicsHomeworkSerializers(locations, many=True)

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
        locations = self.get_post(pk)
        serializer = MathematicsHomeworkSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
