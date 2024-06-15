from django.db import connection
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
import catalog.models
from .forms import ChartForm


def get_sales_info(item_id=0):
    labels = []
    data = []
    item_name = None

    if item_id != 0:
        item_name = str(catalog.models.Item.objects.get(id=item_id))

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT TO_CHAR(DATE_TRUNC('day', catalog_order.time), 'DD/MM/YYYY') d, COUNT(catalog_orderitem.item_id) sales_count \
                FROM catalog_orderitem JOIN catalog_order ON catalog_orderitem.order_id = catalog_order.id \
                WHERE item_id = {item_id} \
                GROUP BY catalog_orderitem.item_id, d"
            )
            rows = cursor.fetchall()

        for row in rows:
            date = row[0]
            sales_count = row[1]
            labels.append(date)
            data.append(sales_count)

    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT TO_CHAR(DATE_TRUNC('day', catalog_order.time), 'DD/MM/YYYY') d, COUNT(catalog_orderitem.item_id) sales_count \
                FROM catalog_orderitem JOIN catalog_order ON catalog_orderitem.order_id = catalog_order.id \
                GROUP BY d"
            )
            rows = cursor.fetchall()

        for row in rows:
            date = row[0]
            sales_count = row[1]
            labels.append(date)
            data.append(sales_count)

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
