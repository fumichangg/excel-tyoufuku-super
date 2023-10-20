import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ExcelForm
from .models import ExcelFile

def process_excel(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save()
            df = pd.read_excel(excel_file.file.path)
            column_name = form.cleaned_data['column_name']
            df = df.drop_duplicates(subset=[column_name])
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=result.xlsx'
            df.to_excel(response, index=False, engine='openpyxl')
            return response
    else:
        form = ExcelForm()
    return render(request, 'excelapp/process_excel.html', {'form': form})
