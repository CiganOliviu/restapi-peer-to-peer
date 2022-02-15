from django.shortcuts import redirect

from AppLayout import update_model_content
from InformaticsDepartment.models import InformaticsSchedule, InformaticsHomework
from MathematicsDepartment.models import MathSchedule, MathHomework
from RomanianDepartment.models import RomanianSchedule, RomanianHomework


def index(request):

    update_model_content.fetch_schedule_model(InformaticsSchedule)
    update_model_content.fetch_schedule_model(MathSchedule)
    update_model_content.fetch_schedule_model(RomanianSchedule)
    update_model_content.fetch_homework_model(InformaticsHomework)
    update_model_content.fetch_homework_model(MathHomework)
    update_model_content.fetch_homework_model(RomanianHomework)

    return redirect('/admin')
