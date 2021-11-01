from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import *


class DomainLister(APIView):

    def get(self, request, format=None):
        locations = Domain.objects.all()
        serializer = DomainSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DomainSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DomainDetail(APIView):

    def get_post(self, pk):
        try:
            return Domain.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = DomainSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = DomainSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class HighSchoolProfileLister(APIView):

    def get(self, request, format=None):
        locations = HighSchoolProfile.objects.all()
        serializer = HighSchoolProfileSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HighSchoolProfileSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HighSchoolProfileDetail(APIView):

    def get_post(self, pk):
        try:
            return HighSchoolProfile.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = HighSchoolProfileSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = HighSchoolProfileSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TownLister(APIView):

    def get(self, request, format=None):
        locations = Town.objects.all()
        serializer = TownSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TownSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TownDetail(APIView):

    def get_post(self, pk):
        try:
            return Town.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = TownSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = TownSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UniversitieLister(APIView):

    def get(self, request, format=None):
        locations = Universitie.objects.all()
        serializer = UniversitieSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UniversitieSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UniversitiesDetail(APIView):

    def get_post(self, pk):
        try:
            return Universitie.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = UniversitieSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = UniversitieSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FacultieLister(APIView):

    def get(self, request, format=None):
        locations = Facultie.objects.all()
        serializer = FacultieSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacultieSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultieDetail(APIView):

    def get_post(self, pk):
        try:
            return Facultie.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = FacultieSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = FacultieSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PositionLister(APIView):

    def get(self, request, format=None):
        locations = Position.objects.all()
        serializer = PositionSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PositionSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionDetail(APIView):

    def get_post(self, pk):
        try:
            return Position.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = PositionSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = PositionSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLister(APIView):

    def get(self, request, format=None):
        locations = User.objects.all()
        serializer = UserSerializers(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_post(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = UserSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = UserSerializers(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response({
            "user": UserSerializers(user).data,
            "token": AuthToken.objects.create(user)[1]
        })