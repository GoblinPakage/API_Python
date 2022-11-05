from RequestResp import Response
import requests

class IMDb_request:
    API_KEY="k_5ih8v2uw"
    _base_url =f"https://imdb-api.com/en/API/SearchSeries/{API_KEY}"
    _base_url_ranking =f"https://imdb-api.com/en/API/Ratings/{API_KEY}"
    
        
    @classmethod
    def get_Movies(cls,Movie):
        response =  requests.get(cls._base_url+"/{}".format(Movie))
        return Response(status_code=response.status_code, content=response.json())
    @classmethod
    def get_Ranking(cls,idMovie):
        response =  requests.get(cls._base_url_ranking+"/{}".format(idMovie))
        return Response(status_code=response.status_code, content=response.json())