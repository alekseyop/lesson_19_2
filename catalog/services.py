from django.core.cache import cache
from catalog.models import Product, Category
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

def get_category_from_cach():
    '''
    Получение категорий из кэша, если кэш включен, если не включен - из базы данных
    '''
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'catalog_list'
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Category.objects.all()
    cache.set(key, catalog)
    return catalog

