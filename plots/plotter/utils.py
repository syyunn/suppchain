import datetime

def change_to_datetime(date_string):
    year = None
    month = None
    date = None
    splits = date_string.split("/")
    if len(splits[0]) == 2 and len(splits[2]) == 4:
        year = splits[2]
        month = splits[0]
        day = splits[1]
        date = datetime.date(
            year=int(year),
            month=int(month[0].replace("0", "") + month[1]),
            day=int(day[0].replace("0", "") + day[1]),
        )
        return date
    elif len(splits[0]) == 4:
        year = splits[0]
        month = splits[1]
        day = splits[2]
        date = datetime.date(
            year=int(year),
            month=int(month[0].replace("0", "") + month[1]),
            day=int(day[0].replace("0", "") + day[1]),
        )
        return date
    else:
        assert len("hi") != 2
