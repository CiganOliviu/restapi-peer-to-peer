from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Stats.serializers import *


class ClientLister(APIView):

    def get(self, request, format=None):
        data_objects = Client.objects.all()
        serializer = ClientSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetails(APIView):

    def get_post(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ClientSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ClientSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherLister(APIView):

    def get(self, request, format=None):
        data_objects = Teacher.objects.all()
        serializer = TeacherSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetails(APIView):

    def get_post(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = TeacherSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = TeacherSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffLister(APIView):

    def get(self, request, format=None):
        data_objects = Staff.objects.all()
        serializer = StaffSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetails(APIView):

    def get_post(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = StaffSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = StaffSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeLister(APIView):

    def get(self, request, format=None):
        data_objects = Income.objects.all()
        serializer = IncomeSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetails(APIView):

    def get_post(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = IncomeSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = IncomeSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseLister(APIView):

    def get(self, request, format=None):
        data_objects = Expense.objects.all()
        serializer = ExpenseSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenseSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetails(APIView):

    def get_post(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ExpenseSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ExpenseSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FeedbackLister(APIView):

    def get(self, request, format=None):
        data_objects = Feedback.objects.all()
        serializer = FeedbackSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedbackSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackDetails(APIView):

    def get_post(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = FeedbackSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = FeedbackSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherExpectationLister(APIView):

    def get(self, request, format=None):
        data_objects = TeacherGoal.objects.all()
        serializer = TeacherGoalsSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherGoalsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherExpectationDetails(APIView):

    def get_post(self, pk):
        try:
            return TeacherGoal.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = TeacherGoalsSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = TeacherGoalsSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentExpectationLister(APIView):

    def get(self, request, format=None):
        data_objects = StudentExpectation.objects.all()
        serializer = StudentExpectationSerializers(data_objects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentExpectationSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentExpectationDetails(APIView):

    def get_post(self, pk):
        try:
            return StudentExpectation.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = StudentExpectationSerializers(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = StudentExpectationSerializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
