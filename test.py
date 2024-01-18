from datetime import datetime

import pytz
from icalendar import Calendar, Event

# Add subcomponents
event = Event()
event.add('name', 'Meeting #001')
event.add('description', 'This is a meeting')
event.add('dtstart', datetime(2024, 1, 25, 8, 0, 0, tzinfo=pytz.timezone('Asia/Taipei')))
event.add('dtend', datetime(2024, 1, 25, 10, 0, 0, tzinfo=pytz.timezone('Asia/Taipei')))

cal = Calendar()
cal.add_component(event)

with open('test.ics', 'wb') as f:
    f.write(cal.to_ical())
