# instructions
# Given a moment, determine the moment that would be after a gigasecond has passed.

# A gigasecond is 10^9 (1,000,000,000) seconds.

from datetime import datetime
from datetime import timedelta
def add(moment):
    gigasecond = 10**9
    moment+=timedelta(seconds = gigasecond)
    return moment