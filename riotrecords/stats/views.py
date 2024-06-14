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
#           .annotate(date=TruncDay("time"))
#           .values("date")
#           .annotate(dcount=Count("date"))
#           )
#
# for order in orders:
#     print(order)

#
# print("------------------------------------------------\n\n")


def get_total_sales(request):

    # В orders хранится пары <дата с точностью до дня, сколько заказов выполнено в этот день>
    orders = (catalog.models.Order.objects
              .filter(status="DE")
              .annotate(date=TruncDay("time"))
              .values("date")
              .annotate(sale_count=Count("date"))
              )

    labels = []
    data = []

    for order in orders:
        date = order["date"].strftime("%D")
        sale_count = order["sale_count"]
        labels.append(date)
        data.append(sale_count)


    return render(request, "stats/charts.html", context={
        "labels": labels,
        "data": data
    })


def get_item_sales(request, item_id):
    # TODO
    # Return sales of current item
    return HttpResponse()
