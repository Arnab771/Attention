from daterange import daterange
import re
import datetime
import matplotlib.pyplot as plt


def split_stat(file_name, A, B):
    file = open(file_name, 'r')

    def get_data(file, person):
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
                    end_date = datetime.datetime.strptime(
                        date, "%m/%d/%y").date()

                if date in stats and person in listLines[i][16:30]:
                    stats[date] += 1
                if date not in stats and person in listLines[i][16:30]:
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
        return [datelist, no_of_mssgs]

    A_info = get_data(file, A)
    file.seek(0, 0)
    B_info = get_data(file, B)
    fig = plt.figure(figsize=(16, 10))
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.plot(
        [f"{date:%-m}/{date:%-d}/{date:%y}" for date in A_info[0]], A_info[1], label=A, color='g')
    ax1.plot(
        [f"{date:%-m}/{date:%-d}/{date:%y}" for date in B_info[0]], B_info[1], label=B, color='m')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(90)
    plt.xlabel("Date")
    plt.ylabel("No. of Messages")
    plt.legend()
    plt.title(f"{A} and {B} Chat")
    plt.show()
