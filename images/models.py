from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from django.db import models

from images.elasticsearch import connection


class ElasticImage(Document):
    bearbeitet_bild = Text(fields={"keyword": Keyword()})
    bildnummer = Integer()
    breite = Integer()
    datum = Date()
    db = Keyword()
    description = Text(fields={"keyword": Keyword()})
    fotografen = Keyword()
    hoehe = Integer()
    suchtext = Text(
        fields={
            "english": Text(analyzer="english"),
            "german": Text(analyzer="german"),
        }
    )
    title = Text(fields={"keyword": Keyword()})

    class Index:
        name = "imago"
        using = connection


class Image(models.Model):
    bearbeitet_bild = models.TextField()
    bildnummer = models.IntegerField()
    breite = models.IntegerField()
    datum = models.DateTimeField()
    db = models.TextField()
    description = models.TextField()
    fotografen = models.TextField()  # this should be a separate Model eventually
    hoehe = models.IntegerField()
    suchtext = models.TextField()
    title = models.TextField()
