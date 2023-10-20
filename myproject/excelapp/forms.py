from django import forms
from .models import ExcelFile

class ExcelForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file', 'column_name')
    column_name = forms.CharField(max_length=100, label='カラム名')