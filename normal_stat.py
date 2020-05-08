from daterange import daterange
import re
import datetime
import matplotlib.pyplot as plt


def normal_stat(file_name):
    file = open(file_name, 'r')
    start_date = 0
    end_date = 0

    stats = {}
    datelist = []
    listLines = file.readlines()
    for i in range(len(listLines)):
        try:
            date = re.compile(
                "^(\d{1,2}\/\d{1,2}\/\d{1,2})").search(listLines[i]).group(1)
            if i == 0:
                start_date = datetime.datetime.strptime(
                    date, "%m/%d/%y").date()
            if i == len(listLines)-1:
                end_date = datetime.datetime.strptime(date, "%m/%d/%y").date()

            if date in stats:
                stats[date] += 1
            else:
                stats[date] = 1
        except AttributeError:
            continue

    datelist = [x for x in daterange(start_date, end_date)]
    no_of_mssgs = []
    for i in datelist:
        if f"{i:%-m}/{i:%-d}/{i:%y}" in stats:
            no_of_mssgs.append(stats[f"{i:%-m}/{i:%-d}/{i:%y}"])
        else:
            no_of_mssgs.append(0)
    fig = plt.figure(figsize=(16, 10))
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.plot(
        [f"{date:%-m}/{date:%-d}/{date:%y}" for date in datelist], no_of_mssgs)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(90)
    plt.xlabel("Date")
    plt.ylabel("No. of Messages")
    plt.show()
