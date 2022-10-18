# github_request.py
import requests
import Response

class GithubRequest:
    _base_url = "https://api.github.com"
        
    @classmethod
    def get_events(cls):
        response =  requests.get(cls._base_url+"/events")
        
        return Response(status_code=response.status_code, content=response.json())