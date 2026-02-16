import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

from datetime import time
time.fromisoformat('04:23:01')

time.fromisoformat('T04:23:01')

time.fromisoformat('T042301')

time.fromisoformat('04:23:01.000384')

time.fromisoformat('04:23:01,000384')

time.fromisoformat('04:23:01+04:00')

time.fromisoformat('04:23:01Z')

time.fromisoformat('04:23:01+00:00')

from datetime import time
time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')

dt = time(hour=12, minute=34, second=56, microsecond=0)
dt.isoformat(timespec='microseconds')

dt.isoformat(timespec='auto')