# main.py

import VersioningEventFacade
import VersioningEvent

versioning_events = VersioningEventFacade.get_versioning_events()

for versioning_event in versioning_events:
    assert isinstance(versioning_event, VersioningEvent)
    
print("ok")
# I cant now work with Python Objects