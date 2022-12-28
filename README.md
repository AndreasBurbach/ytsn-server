# YouTube - The Social Network

This package is a django base backend server which includes [The Social Network](https://pypi.org/project/the-social-network/)
It extends the-scoial-network to save statements for the transcript of a YouTube video.

## Installation
Minimum requierments are:

> [Python](https://www.python.org/downloads/) >= 3.9
> [Django](https://pypi.org/project/Django/) >= 3.2.9
> [Pillow](https://pypi.org/project/Pillow/) >= 8.4.0
> [django-cors-headers](https://pypi.org/project/django-cors-headers/) >= 3.10.0
> [djangorestframework](https://pypi.org/project/djangorestframework/) >= 3.12.4
> [django-dotenv](https://pypi.org/project/django-dotenv/) >= 1.4.2
> [The Social Network](https://pypi.org/project/the-social-network/) >= 0.0.7
> [psycopg2-binary](https://pypi.org/project/psycopg-binary/) >= 3.1.6
> [whitenoise](https://pypi.org/project/whitenoise/) >= 6.2.0

## How to use

Create the database with
> python manage.py migrate

and start the server with
> python manage.py runserver

the default page should showup if you open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Request API for the URLs

In all requests (except for the request of *authentication/register/* or */authentication/login/*) you need to send the authentification token inside the header.
For authorization use the header name "Authorization" and the value "Token <token>".
This interface only extends the interfaces of "the-social-network".

#### POST url: ".../youtubeStatement/getCommentsByVideoAndTime/"
Get statements with query to videoId of youtube and time inside the transcript  

Requestbody:  
```json
{  
    "youtubeVideoId": "youtubeVideoId",  
    "videoTime": "01:23"
} 
``` 
Responsebody:  
```json
{ 
    "data":[
        {
            "videoTime": "01:23",
            "statement": "statementId",
            "vote": "vote"
        }
    ]
}  
```

#### POST url: ".../youtubeStatement/getCommentsByVideo/"
Get all statements for the transcript of a videoId of youtube

Requestbody:  
```json
{  
    "youtubeVideoId": "youtubeVideoId"
}  
```
Responsebody:  
```json
{ 
    "data":[
        {
            "videoTime": "01:23",
            "statement": "statementId",
            "vote": "vote"
        }
    ]
}    
```

#### POST url: ".../youtubeStatement/add/"
Creates a statement inside of a transcript of a youtube video

Requestbody:  
```json
{  
    "youtubeVideoId": "youtubeVideoId",
    "videoTime": "01:23",
    "input": "statement",
    "vote": "vote"
}  
```
Responsebody:
(Array has length 1)

```json
{ 
    "data":[
        {
            "videoTime": "01:23",
            "statement": "statementId",
            "vote": "vote"
        }
    ]
}    
```


## Core Database structure

The project requieres the base database structure of the-social-network and extends it by adding just one new table 

#### YoutubeVideoStatement
    with  
    video_id: varchar(100) as primary key
    statement: int as foreign key to the_social_network_statement
    videoTime: varchar(100)
    vote: small uint