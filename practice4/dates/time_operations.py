from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta)

from datetime import timedelta
d = timedelta(microseconds=-1)
print

from datetime import timedelta
duration = timedelta(seconds=11235813)
print(duration.days, duration.seconds
)
print(duration.total_seconds())
print(d.days, d.seconds, d.microseconds)

from datetime import time, tzinfo, timedelta
class TZ1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self,dt):
        return "+01:00"
    def  __repr__(self):
        return f"{self.__class__.__name__}()"

t = time(12, 10, 30, tzinfo=TZ1())
t

t.isoformat()

t.dst()

t.tzname()

t.strftime("%H:%M:%S %Z")

'The {} is {:%H:%M}.'.format("time", t)