from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models.functions import TruncDay, TruncMonth
from django.db.models import Count
import catalog.models

print("\n\n----------- IN STATS VIEW TEST -----------------")

# Get all sales (delivered orders) from database
item_id = 8
orders_id = (catalog.models.OrderItem.objects
             .filter(item_id=item_id)
             .values_list("order_id")
             )

orders = (catalog.models.Order.objects
          .filter(id__in=orders_id, status="DE")
          .annotate(date=TruncDay("time"))
          .values("date")
          .annotate(sale_count=Count("date"))
          )

for order in orders:
    print(order)

print("------------------------------------------------\n\n")


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
    # Orders with specified item
    orders_id = (catalog.models.OrderItem.objects
                 .filter(item_id=item_id)
                 .values_list("order_id")
                 )

    orders = (catalog.models.Order.objects
              .filter(id__in=orders_id, status="DE")
              .annotate(date=TruncDay("time"))
              .values("date")
              .annotate(sale_count=Count("date"))
              )

    labels = []
    data = []
    item_name = str(catalog.models.Item.objects.get(id=item_id))

    for order in orders:
        date = order["date"].strftime("%D")
        sale_count = order["sale_count"]
        labels.append(date)
        data.append(sale_count)

    return render(request, "stats/charts.html", context={
        "labels": labels,
        "data": data,
        "item_name": item_name
    })
