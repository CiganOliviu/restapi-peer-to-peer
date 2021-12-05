from django.contrib import admin
from InformaticsDepartment.models import (
    InformaticsGroup,
    InformaticsSchedule,
    InformaticsHomework
)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'responsible_teacher')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'course_title', 'deadline_date', 'dated')
    list_filter = ('deadline_date', 'dated', )
    exclude = ('dated', )


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'title', 'deadline_date', 'dated', 'optional', 'posted_on')
    exclude = ('teacher', 'dated')
    ordering = ('posted_on',)
    list_filter = ('deadline_date', 'dated', 'optional')

    def save_model(self, request, obj, form, change):
        obj.teacher = request.user
        obj.save()


admin.site.register(InformaticsGroup, GroupAdmin)
admin.site.register(InformaticsSchedule, ScheduleAdmin)
admin.site.register(InformaticsHomework, HomeworkAdmin)
