from app.models.schemas import Event
def analyze_event(event:Event):
    return{
        "title":event.title,
        "domain":event.domain,
        "location":event.location
    }