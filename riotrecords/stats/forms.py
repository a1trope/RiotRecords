from django import forms

class ChartForm(forms.Form):
    # template_name = "stats/form_snippet.html"

    # TODO: make select for all item in catalog
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    item_field = forms.ChoiceField(label="Выберите товар", choices=CHOICES)