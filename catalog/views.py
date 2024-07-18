from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    item_name = Product.objects.all()
    context = {
        'items': item_name
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product = Product.objects.get(pk=pk)
    context = {"item": product}
    return render(request, 'catalog/product_detail.html', context)
