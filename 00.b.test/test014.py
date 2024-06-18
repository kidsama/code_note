import traceback
from datetime import datetime

def timestampToString(milliseconds_timestamp):
    date_obj = None
    try:
        seconds_timestamp = milliseconds_timestamp / 1000
        run_date = datetime.fromtimestamp(seconds_timestamp)
        date_obj = run_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        traceback.print_exc()
    finally:
        return date_obj

aaa = timestampToString(1715503922937)
print(aaa, type(aaa))
