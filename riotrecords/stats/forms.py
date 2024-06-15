from django import forms
import catalog.models

class ChartForm(forms.Form):
    CHOICES = [(0, "-- Выберите товар --")]

    items = catalog.models.Item.objects.all().order_by("id")
    for item in items:
        CHOICES.append((item.id, str(item)))

    item_field = forms.ChoiceField(label="Выберите товар", choices=CHOICES)