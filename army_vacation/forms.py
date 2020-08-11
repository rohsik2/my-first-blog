from django import forms
from .models import Vacation


class VacationForm(forms.ModelForm):
    start_date = forms.DateField(help_text="ex) 12/31/2020");
    end_date = forms.DateField(help_text="ex) 12/31/2020");
    reason = forms.ChoiceField(choices=Vacation.SORT_OF_VACATIONS)
    
    class Meta:
        model = Vacation
        fields = ('start_date', 'end_date', 'reason')