from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def get_total_sales(request):
    labels = []
    data = []

    # TODO: Get all sales from database

    return render(request, "stats/charts.html", context={
        "labels": labels,
        "data": data
    })


def get_item_sales(request, item_id):
    # TODO
    # Return sales of current item
    return HttpResponse()
