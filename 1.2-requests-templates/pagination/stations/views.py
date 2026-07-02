import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from functools import lru_cache


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    LIMIT = 25
    page_number = request.GET.get('page', "")
    page_number = int(page_number) if page_number.isdigit() else 1

    paginator = Paginator(_read_stations(), LIMIT)

    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)


@lru_cache(maxsize=1)
def _read_stations() -> list:
    try:
        with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as data:
            reader = csv.DictReader(data)
            return list(reader)
    except Exception as e:
        print(f"File I/O error: {e}")
        return []
