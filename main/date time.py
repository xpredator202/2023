import datetime


def date():
    """just return date as string
    : return date if success, false if faild
    """

    try: 
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    return date


def time():
    """
    just return time as string
     : return : time if success, false if fail
     """
    try: 
        time = datetime.datetime.now().strftime("%H:%M:%S")
    except Exception as e:
        print(e)
        date = False
    return time