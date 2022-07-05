from django import forms
import datetime
class DatewiseView(forms.Form):
    search_Day = forms.DateField(required=True,initial=datetime.date.today)

