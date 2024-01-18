from datetime import datetime

import pytz
from icalendar import Calendar, Event

cal = None

with open('test.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())
    
# Add subcomponents
event = Event()
event.add('name', 'Meeting 002')
event.add('description', 'This is aother meeting')
event.add('dtstart', datetime(2024, 1, 27, 8, 0, 0, tzinfo=pytz.timezone('Asia/Taipei')))
event.add('dtend', datetime(2024, 1, 27, 10, 0, 0, tzinfo=pytz.timezone('Asia/Taipei')))

cal.add_component(event)

with open('test2.ics', 'wb') as f:
    f.write(cal.to_ical())
