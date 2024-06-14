from django import forms

class ChartForm(forms.Form):
    template_name = "stats/form_snippet.html"

    # TODO: make select for all item in catalog
    item = forms.Select(
        choices={
            "a": "1",
            "b": "2",
            "c": "3",
        }
    )