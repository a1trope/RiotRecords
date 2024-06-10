from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def get_total_sales(request, time):
    # Return total sales for the last month
    return HttpResponse()


def get_item_sales(request, item_id):
    # Return sales of current item
    return HttpResponse()
