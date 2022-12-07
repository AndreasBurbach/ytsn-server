from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
    
from youtube.views import YoutubeStatementShowAll, YoutubeStatementAdd, YoutubeStatementGetCommentsByYoutubeUrl

urlpatterns = [
    path('getCommentsByVideoAndTime/', YoutubeStatementShowAll.as_view(), name='getCommentsByVideoAndTime'),
    path('getCommentsByVideo/', YoutubeStatementGetCommentsByYoutubeUrl.as_view(), name='getCommentsByVideo'),
    path('add/', YoutubeStatementAdd.as_view(), name='add'),
]
