from datetime import datetime, timezone
datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()

datetime(2019, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat()

from datetime import tzinfo, timedelta, datetime
class TZ(tzinfo):
    """A time zone with an arbitrary, constant -06:39 offset."""
    def utcoffset(self, dt):
        return timedelta(hours=-6, minutes=-39)

datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')

datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
from datetime import timedelta, datetime, tzinfo, timezone

class KabulTz(tzinfo):
    # Kabul used +4 until 1945, when they moved to +4:30
    UTC_MOVE_DATE = datetime(1944, 12, 31, 20, tzinfo=timezone.utc)

    def utcoffset(self, dt):
        if dt.year < 1945:
            return timedelta(hours=4)
        elif (1945, 1, 1, 0, 0) <= dt.timetuple()[:5] < (1945, 1, 1, 0, 30):
            # An ambiguous ("imaginary") half-hour range representing
            # a 'fold' in time due to the shift from +4 to +4:30.
            # If dt falls in the imaginary range, use fold to decide how
            # to resolve. See PEP495.
            return timedelta(hours=4, minutes=(30 if dt.fold else 0))
        else:
            return timedelta(hours=4, minutes=30)

    def fromutc(self, dt):
        # Follow same validations as in datetime.tzinfo
        if not isinstance(dt, datetime):
            raise TypeError("fromutc() requires a datetime argument")
        if dt.tzinfo is not self:
            raise ValueError("dt.tzinfo is not self")

        # A custom implementation is required for fromutc as
        # the input to this function is a datetime with utc values
        # but with a tzinfo set to self.
        # See datetime.astimezone or fromtimestamp.
        if dt.replace(tzinfo=timezone.utc) >= self.UTC_MOVE_DATE:
            return dt + timedelta(hours=4, minutes=30)
        else:
            return dt + timedelta(hours=4)

    def dst(self, dt):
        # Kabul does not observe daylight saving time.
        return timedelta(0)

    def tzname(self, dt):
        if dt >= self.UTC_MOVE_DATE:
            return "+04:30"
        return "+04"
    

tz1 = KabulTz()

# Datetime before the change
dt1 = datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
print(dt1.utcoffset())


# Datetime after the change
dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
print(dt2.utcoffset())


# Convert datetime to another time zone
dt3 = dt2.astimezone(timezone.utc)
dt3

dt2

dt2 == dt3