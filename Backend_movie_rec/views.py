from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import *
import pickle
import pandas as pd
import numpy
from .functions import req_data
import json
movies_lis = pickle.load(open('movie_data/Movie_rec.pkl','rb'))
similarity = pd.DataFrame(pickle.load(open('movie_data/Similarity.pkl','rb')))
movies = pd.DataFrame(movies_lis)
def recommend(movie):
  print('heyyyyyyyyyyy')
  index = movies[movies['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
  lis = {}
  lis['title'] = []
  lis['movie_id'] = []
  for i in distances[1:5]:
    lis['title'].append(str(movies.iloc[i[0]].title))
    lis['movie_id'].append(str(movies.iloc[i[0]].movie_id))
  print(lis)
  return lis

print(movies['title'].values)


@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def Movies(request):
    try:
        movie = request.data.get('movie', 'Batman')
        print(movie)
        sim = recommend(movie)
        print(sim)
        sim['pics'] = []
        for movie_id in sim['movie_id']:
            sim['pics'].append(req_data(movie_id))
        print(sim)
        return Response(sim, status=status.HTTP_200_OK)
    except Exception as e:
        print(str(e))
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def signup(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    user = User.objects.get(username=request.data['username'])
    user.set_password(request.data['password'])
    user.save()
    token = Token.objects.create(user=user)
    return Response({'token': token.key,'user': serializer.data})
  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
  user = get_object_or_404(User,username=request.data['username'])
  if not user.check_password(request.data['password']):
    return Response({'details':"Username or password not valid"},status=status.HTTP_404_NOT_FOUND)
  token,created = Token.objects.get_or_create(user=user)
  return Response({"token":token.key})

