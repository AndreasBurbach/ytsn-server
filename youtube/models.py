from django.db import models

# Create your models here.

class YoutubeVideoStatement(models.Model):
    video_id = models.CharField(max_length=100, blank=False, db_index=True)
    statement = models.ForeignKey('the_social_network.Statement', on_delete=models.CASCADE)
    videoTime = models.CharField(max_length=100, blank=False, db_index=True)
    vote = models.PositiveSmallIntegerField(
        choices=[
            (1, "like"),
            (2, "dislike")
        ],
        default=1
    )