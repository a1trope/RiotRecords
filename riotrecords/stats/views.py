from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.db.models.functions import TruncDay, TruncMonth
from django.db.models import Count
import catalog.models
from .forms import ChartForm


# print("--------------- TEST IN STATS ---------------")
#
# items = catalog.models.Item.objects.all().order_by("id")
# choices = []
#
# for item in items:
#     choices.append((item.id, str(item)))
#
# print(choices)
#
# # print(items)
#
# print("---------------------------------------------")

def get_sales_info(item_id=0):
    labels = []
    data = []
    item_name = None

    if item_id != 0:
        item_name = str(catalog.models.Item.objects.get(id=item_id))

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

    else:
        orders = (catalog.models.Order.objects
                  .filter(status="DE")
                  .annotate(date=TruncDay("time"))
                  .values("date")
                  .annotate(sale_count=Count("date"))
                  )

    for order in orders:
        date = order["date"].strftime("%D")
        sale_count = order["sale_count"]
        labels.append(date)
        data.append(sale_count)

    return labels, data, item_name


@staff_member_required(login_url="accounts:login", redirect_field_name='next')
def get_total_sales(request):
    labels = []
    data = []
    item_name = None
    form = ChartForm

    if request.method == "GET":
        labels, data, _ = get_sales_info()

    if request.method == "POST":
        form = ChartForm(request.POST)
        item_id = int(request.POST["item_field"])

        labels, data, item_name = get_sales_info(item_id)

    return render(request, "stats/charts.html", context={
        "labels": labels,
        "data": data,
        "item_name": item_name,
        "form": form
    })
