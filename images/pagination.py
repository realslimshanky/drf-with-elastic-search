from rest_framework.pagination import LimitOffsetPagination


class ImagePagination(LimitOffsetPagination):
    default_limit = 10

    def get_count(self, query):
        try:
            return query.count()
        except (AttributeError, TypeError):
            return len(query)

    def paginate_query(self, query, request):
        self.request = request
        self.count = self.get_count(query)

        self.limit = self.get_limit(request)
        if self.limit > 10000:
            self.limit = 10000

        self.offset = self.get_offset(request)
        if self.offset + self.limit > 10000:
            # ElasticSearch Index - "Imago" Limitation
            self.offset = 10000 - self.limit

        return query.extra(from_=self.offset, size=self.limit)
