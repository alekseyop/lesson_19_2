from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_product_from_cache():
    """
    Возвращает список продуктов из кэша,
    если кэш не используется,
    то возвращает список продуктов из БД
     """
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = 'products'
    product = cache.get("key")

    if product is None:
        product = Product.objects.all()
        cache.set(key, product)
    return product

