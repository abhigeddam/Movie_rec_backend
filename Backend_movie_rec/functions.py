import requests
import json

def req_data(data):
  print(data)

  url = "https://api.themoviedb.org/3/movie/"+str(data)+"?language=en-US"
  headers = {
    "accept": "application/json",
    "Authorization": "Bearer"
    }
  response = requests.get(url, headers=headers).json()
  print(response)
  
  return "https://image.tmdb.org/t/p/w500/"+response['poster_path']

