import datetime
def date_in_future(day = 'aaa'):
    tod = datetime.datetime.now()
    if type(day) is int:
        tod += datetime.timedelta(days=day)
    tod = tod.strftime("%Y-%m-%d %H:%M:%S")
    print(str(tod))
    return 
date_in_future()
date_in_future(1)
