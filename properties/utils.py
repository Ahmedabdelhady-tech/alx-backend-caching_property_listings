from django.core.cache import cache
from .models import Property


def get_all_properties():
    properties = cache.get("all_properties")
    if not properties:
        properties = list(
            Property.objects.all().values("id", "title", "price", "address")
        )
        cache.set("all_properties", properties, timeout=3600)
    return properties
