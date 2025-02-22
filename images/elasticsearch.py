from django.conf import settings
from elasticsearch_dsl import connections


connection = connections.create_connection(
    hosts=settings.ELASTIC_HOST,
    basic_auth=(settings.ELASTIC_USER, settings.ELASTIC_PASS),
    verify_certs=False,
)
