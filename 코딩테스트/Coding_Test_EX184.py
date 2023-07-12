import datetime as dt

def solution(date1, date2):
    time1 = dt.datetime(date1[0], date1[1], date1[2])
    time2 = dt.datetime(date2[0], date2[1], date2[2])
    if time1 >= time2:
        return 0
    else:
        return 1

print(solution([2021, 12, 28], [2021, 12, 29]))