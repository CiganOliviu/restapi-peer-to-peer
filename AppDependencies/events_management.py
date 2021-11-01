from datetime import date


def get_current_time():
    result = date.today()

    return result


def is_event_out_of_day(event_day):
    current_day = get_current_time().day

    if current_day > event_day:
        return True

    return False


def is_the_day_match(event_day):
    current_day = get_current_time().day

    if current_day == event_day:
        return True

    return False


def is_event_out_of_month(event_month):
    current_month = get_current_time().month

    if current_month > event_month:
        return True

    return False


def is_the_month_match(event_month):
    current_month = get_current_time().month

    if current_month == event_month:
        return True

    return False


def is_event_out_of_year(event_year):
    current_year = get_current_time().year

    if current_year > event_year:
        return True

    return False


def is_the_year_match(event_year):
    current_year = get_current_time().year

    if current_year == event_year:
        return True

    return False


def check_if_event_is_dated(event):
    if is_event_out_of_year(event.deadline_date.year):
        return True

    if is_the_year_match(event.deadline_date.year):
        if is_event_out_of_month(event.deadline_date.month):
            return True

    if is_the_month_match(event.deadline_date.month):
        if is_event_out_of_day(event.deadline_date.day):
            return True

    return False

