
# VersioningEvent.py
from IMDb_request import IMDb_request
class Movie:
    
    def __init__(self,id,resultType,image,title,description):
        self.id = id
        self.resultType = resultType
        self.image = image
        self.title = title
        self.description = description

class MovieFacade:

     
    def get_id_Movie(text):

        movies =  IMDb_request.get_Movies(text).content
        
        movies=movies["results"]
        versioning_event=[]
        for movie in movies:
            versioning_event.append( Movie(id=movie["id"], resultType=movie["resultType"],image=movie["image"],title=movie["title"],description=movie["description"]))
        return versioning_event[0].id
    
    def getRanking(idMovie):

        ranking = IMDb_request.get_Ranking(idMovie=idMovie).content
        return ranking['theMovieDb']