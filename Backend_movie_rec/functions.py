import requests
import json

def req_data(data):
  print(data)

  url = "https://api.themoviedb.org/3/movie/"+str(data)+"?language=en-US"
  headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTFhZWYxZDQ3OWE4ZWE4MDA2YjEyNWVhM2MwNTlkMCIsIm5iZiI6MTcyMzY3NTQxNC4wODc1NjQsInN1YiI6IjY1ZGYxZjE3OGU4NzAyMDE4NDA0ZTA3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mAk46DbbGYJkHdOi3aWb4kQfFzIp3MYWFXyZ07-oNLE"
    }
  response = requests.get(url, headers=headers).json()
  print(response)
  
  return "https://image.tmdb.org/t/p/w500/"+response['poster_path']

