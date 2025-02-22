from django_filters import FilterSet, DateTimeFilter

from images.models import Image


class ImageFilter(FilterSet):
    datum__gte = DateTimeFilter(field_name="datum", lookup_expr="datum__gte")
    datum__lte = DateTimeFilter(field_name="datum", lookup_expr="datum__lte")

    class Meta:
        model = Image
        fields = [field.name for field in Image._meta.fields]
