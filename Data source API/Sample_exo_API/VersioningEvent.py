# VersioningEvent.py
class VersioningEvent:
    
    def __init__(self, type, message, created_at):
        self.type = type
        self.message = message
        self.created_at = created_at

class VersioningEventFacade:

    _base_url = "https://api.github.com"
    
    def get_versioning_events() -> [VersioningEvent]:

        events =  GithubRequest.get_events().content
        
        versioning_event=[]
        for version in events:
            versioning_event.append( VersioningEvent(type=version["type"],message= version["payload"], created_at=version["created_at"]))
        return versioning_event 