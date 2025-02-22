from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from images.filters import ImageFilter
from images.models import ElasticImage, Image
from images.pagination import ImagePagination
from images.serializers import ImageSearchSerializer
from images.utils import get_query_args_from_filter, get_query_type_from_lookup_expr


class ImageSearchView(ListAPIView):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ImageFilter
    queryset = Image.objects.all()
    pagination_class = ImagePagination
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
            query = query.query(
                "multi_match", query=search_term, fields=self.search_fields,
            )

        for filter_name, filter in self.filterset_class.get_filters().items():
            if filter_value:=self.request.GET.get(filter_name):
                query_type = get_query_type_from_lookup_expr(filter.lookup_expr)
                query_args = get_query_args_from_filter(filter_name, filter_value)
                query = query.filter(query_type, **query_args)

        return query

    def list(self, request, *args, **kwargs):
        query = ElasticImage.search()
        query = self._apply_filter(query)
        query = self.paginator.paginate_query(query, request)

        response = query.execute()
        results = [
            ImageSearchSerializer.from_elastic_search(image_response)
            for image_response in response
        ]

        return self.get_paginated_response(results)
