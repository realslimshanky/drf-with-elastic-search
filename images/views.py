from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from images.filters import ImageFilter
from images.models import ElasticImage, Image
from images.serializers import ImageSearchSerializer


class ImageSearchView(ListAPIView):
    filter_backends = [SearchFilter, DjangoFilterBackend]  # Enable filtering on the browsable API
    filterset_class = ImageFilter
    queryset = Image.objects.all()
    search_fields = [
        "bearbeitet_bild.keyword",
        "db",
        "description.keyword",
        "fotografen",
        "title.keyword",
        "suchtext.english",
        "suchtext.german",
    ]

    def _apply_filter(self, query):
        if search_term := self.request.GET.get("search"):
            query = query.query("multi_match", query=search_term, fields=self.search_fields)

        if datum := self.request.GET.get("datum"):
            query = query.query("match", datum=datum)
        if fotografen := self.request.GET.get("fotografen"):
            query = query.query("match", fotografen=fotografen)
        if breite_min := self.request.GET.get("breite_min"):
            query = query.filter("range", breite={"gte": breite_min})
        if breite_max := self.request.GET.get("breite_max"):
            query = query.filter("range", breite={"lte": breite_max})
        return query

    def list(self, request, *args, **kwargs):
        query = ElasticImage.search()
        
        query = self._apply_filter(query)
        response = query.execute()
        results = [
            ImageSearchSerializer.from_elastic_search(image_response)
            for image_response in response
        ]
    
        return Response(results)
