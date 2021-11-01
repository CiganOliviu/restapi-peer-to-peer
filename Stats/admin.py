from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('domain_expertise', )


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    list_filter = ('high_school_profile', )


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('staff', 'income')
    exclude = ('staff',)

    def save_model(self, request, obj, form, change):
        obj.staff = request.user
        obj.save()


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('staff', 'scope', 'expense')
    exclude = ('staff',)

    def save_model(self, request, obj, form, change):
        obj.staff = request.user
        obj.save()


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'faculty', 'position')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'targetTeacher', 'posted_on')


class TeacherExpectationsAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'title', 'posted_on', 'deadline', 'done')
    exclude = ('teacher', )

    def save_model(self, request, obj, form, change):
        obj.teacher = request.user
        obj.save()


class StudentExpectationsAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'posted_on', 'deadline', 'done')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(TeacherExpectation, TeacherExpectationsAdmin)
admin.site.register(StudentExpectation, StudentExpectationsAdmin)


admin.site.site_header = "PTP-Learning Control Panel"
