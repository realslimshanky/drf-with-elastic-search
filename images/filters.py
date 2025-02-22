from django_filters import DateTimeFilter, FilterSet, NumberFilter

from images.models import Image


class ImageFilter(FilterSet):
    datum__gte = DateTimeFilter(field_name="datum", lookup_expr="datum__gte")
    datum__lte = DateTimeFilter(field_name="datum", lookup_expr="datum__lte")
    breite__min = NumberFilter(field_name="breite", lookup_expr="breite__gte")
    breite__max = NumberFilter(field_name="breite", lookup_expr="breite__lte")

    class Meta:
        model = Image
        fields = [field.name for field in Image._meta.fields]
