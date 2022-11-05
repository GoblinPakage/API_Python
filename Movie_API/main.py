# main.py

from Movie import MovieFacade
#import VersioningEvent

''' versioning_events = VersioningEventFacade.get_versioning_events()

for versioning_event in versioning_events:
    assert isinstance(versioning_event, VersioningEvent)
print("ok") '''
movie=input("Enter the name of the movie: ")
id=MovieFacade.get_id_Movie(movie)
print("Film id: %s "%id)
print("Ranking of the film: %s is %s"%(movie,MovieFacade.getRanking(id)))
# I cant now work with Python Objects