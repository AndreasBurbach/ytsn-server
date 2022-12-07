from django.shortcuts import render
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from youtube.models import YoutubeVideoStatement
from the_social_network.models import Statement, Account

from youtube.serializer import YoutubeStatementSerializer

# Create your views here.

class YoutubeStatementShowAll(APIView):
    """
    This view is for getting the transcript of a youtube video.
    The calling user must be authenticated.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request: Request):

        videoTime = request.data.get('videoTime', None)
        if not videoTime:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        youtubeVideoId: str = request.data.get("youtubeVideoId", None)
        if not youtubeVideoId:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        youtubeStatements: QuerySet[YoutubeVideoStatement] = YoutubeVideoStatement.objects.filter(video_id=youtubeVideoId, videoTime=videoTime)
        if not youtubeStatements:
            return Response(status=status.HTTP_204_NO_CONTENT, data=[])

        serializer: youtubeStatements = YoutubeStatementSerializer(instance=youtubeStatements, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class YoutubeStatementGetCommentsByYoutubeUrl(APIView):
    """
    This view is for getting the transcript of a youtube video.
    The calling user must be authenticated.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request: Request):

        youtubeVideoId: str = request.data.get("youtubeVideoId", None)
        if not youtubeVideoId:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        youtubeStatements: QuerySet[YoutubeVideoStatement] = YoutubeVideoStatement.objects.filter(video_id=youtubeVideoId)
        if not youtubeStatements:
            return Response(status=status.HTTP_204_NO_CONTENT, data=[])

        serializer: youtubeStatements = YoutubeStatementSerializer(instance=youtubeStatements, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class YoutubeStatementAdd(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request: Request):
        account: Account = Account.objects.filter(user=request.user).first()

        videoTime: str = request.data.get('videoTime', None)
        if not videoTime:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        statement: str = request.data.get("input", None)
        if not statement:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        vote: str = request.data.get("vote", None)
        if not vote:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        vote: int = 1 if vote == "support" else 2

        youtubeVideoId: str = request.data.get("youtubeVideoId", None)
        if not youtubeVideoId:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        statement: Statement = account.add_statement(statement)

        youtubeStatement = YoutubeVideoStatement.objects.create(video_id=youtubeVideoId, statement=statement, videoTime=videoTime, vote=vote)
        
        serializer = YoutubeStatementSerializer(instance=[youtubeStatement], many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)