from . import events_management as em


def fetch_schedule_model(model):
    data = model.objects.all()

    for event in data:
        if em.check_if_event_is_dated(event):
            model.objects.filter(course_title=event.course_title).update(dated=True)


def fetch_homework_model(model):
    data = model.objects.all()

    for event in data:
        if em.check_if_event_is_dated(event):
            model.objects.filter(title=event.title).update(dated=True)
