from rest_framework import serializers

from images.models import ElasticImage


class ImageSearchSerializer(serializers.Serializer):
    bearbeitet_bild = serializers.CharField()
    bildnummer = serializers.IntegerField()
    breite = serializers.IntegerField()
    datum = serializers.DateTimeField()
    db = serializers.CharField()
    description = serializers.CharField()
    fotografen = serializers.CharField()
    hoehe = serializers.IntegerField()
    suchtext = serializers.CharField()
    title = serializers.CharField()

    @staticmethod
    def from_elastic_search(image: ElasticImage):
        return {
            "bearbeitet_bild": image.bearbeitet_bild,
            "bildnummer": image.bildnummer,
            "breite": image.breite,
            "datum": image.datum,
            "db": image.db,
            "description": image.description,
            "fotografen": image.fotografen,
            "hoehe": image.hoehe,
            "suchtext": image.suchtext,
            "title": image.title,
        }
