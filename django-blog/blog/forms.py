class Meta:
    widgets = {
        "pub_date": forms.widgets.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    }
