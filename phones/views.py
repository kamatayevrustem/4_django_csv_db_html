from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')
    if sort_type == 'min-price':
        phones = Phone.objects.order_by('price')
    elif sort_type == 'max-price':
        phones = Phone.objects.order_by('-price')
    elif sort_type == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__exact=slug)
    context = {'phone': phone}

    return render(request, template, context)
