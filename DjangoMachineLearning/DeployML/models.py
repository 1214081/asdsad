from django.db import models

# Create your models here.


class Preprocessing(models.Model):
    date = models.TimeField()
    tweets = models.CharField(max_length=255)
    clear = models.CharField(max_length=255)
    token_tweets = models.CharField(max_length=255)
    freq_words = models.CharField(max_length=255)
    stemmed_words = models.CharField(max_length=255)
    polarity_score = models.IntegerField()
    polarity = models.CharField(max_length=255)
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'preprocessing'
