from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models.functions import TruncDay, TruncMonth
from django.db.models import Count
import catalog.models

# print("\n\n----------- IN STATS VIEW TEST -----------------")
#
# # Get all sales (delivered orders) from database
# orders = (catalog.models.Order.objects
#           .filter(status="DE")
#           .annotate(day_time=TruncDay("time"))
#           .values("day_time")
#           .annotate(dcount=Count("day_time"))
#               )
#
# for order in orders:
#     print(order)
#
# # print(orders)
#
# print("------------------------------------------------\n\n")


def get_total_sales(request):
    labels = []
    data = []

    # В данной хранится пары <дата с точностью до дня, сколько заказов выполнено в этот день>
    orders = (catalog.models.Order.objects
              .filter(status="DE")
              .annotate(day_time=TruncDay("time"))
              .values("day_time")
              .annotate(dcount=Count("day_time"))
              )

    return render(request, "stats/charts.html", context={
        "labels": labels,
        "data": data
    })


def get_item_sales(request, item_id):
    # TODO
    # Return sales of current item
    return HttpResponse()
