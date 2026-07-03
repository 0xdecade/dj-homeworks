from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort', None)
    sort_case = {
        "name": "name",
        "min_price": "price",
        "max_price": "-price"
    }

    if sort:
        phones = phones.order_by(sort_case.get(sort, "id"))

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {"phone": phone}
    return render(request, template, context)
