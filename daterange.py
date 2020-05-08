import datetime


def daterange(start_date, date2):
    for n in range(int((date2 - start_date).days)+1):
        yield start_date + datetime.timedelta(n)
