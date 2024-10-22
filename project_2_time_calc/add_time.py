def add_time(start, time_to_add,weekday=None):

    start = start.split()
    am_or_pm = start[1]
    start = start[0].split(':')
    hr = int(start[0])
    if am_or_pm == 'PM':
        hr += 12


    minute = int(start[1])
    time_to_add = time_to_add.split(':')
    hr_add = int(time_to_add[0])
    min_add = int(time_to_add[1])
    minute += min_add
    hr += hr_add + (minute // 60)

    if minute > 60:
        minute = minute % 60
    if minute < 10:
        minute = str(minute)
        minute = '0' + minute
    days = hr // 24

    hr = hr % 24
    if hr == 0:
        hr = 12
        am_or_pm = 'AM'
    elif hr == 12:
        if am_or_pm == 'PM':
            am_or_pm = 'AM'
        else:
            am_or_pm = 'PM'
    elif hr < 12:
        am_or_pm = 'AM'
    elif hr > 12:
        hr -= 12
        am_or_pm = 'PM'

    week_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    if weekday != None:
        weekday = weekday.capitalize()
        if weekday in week_dict:
            day_of_week = week_dict[weekday]
        day_of_week += days
        day_of_week = day_of_week % 7
        day_of_week = [key for key, value in week_dict.items() if value == day_of_week]

    if weekday == None:
        if days == 1:
            return(f"{hr}:{minute} {am_or_pm} (next day)")
        elif days > 1:
            return(f"{hr}:{minute} {am_or_pm} ({days} days later)")
        else:
            return(f"{hr}:{minute} {am_or_pm}")
    else:    
        if days == 1:
            return(f"{hr}:{minute} {am_or_pm}, {day_of_week[0]} (next day)")
        elif days > 1:
            return(f"{hr}:{minute} {am_or_pm}, {day_of_week[0]} ({days} days later)")
        else:
            return(f"{hr}:{minute} {am_or_pm}, {day_of_week[0]}")

print(add_time("11:40 AM", "0:25"))