from django.shortcuts import render, HttpResponse
from .backend import json_csv, handle_uploaded_file
from .forms import JsonForm, UploadFileForm

# Create your views here.
def index(request):
    json_form = JsonForm()
    file_form = UploadFileForm()
    csv = ''

    if request.method == 'POST':
        json_form = JsonForm(request.POST)
        file_form = UploadFileForm(request.POST, request.FILES)

        if json_form.is_valid():
            json_str = json_form.cleaned_data['json']
            csv = json_csv(json_str)
            context = {
                'output' : csv
            }
            return render(request, 'app/csv.html', context)
        
        if file_form.is_valid():
            msg = handle_uploaded_file(request.FILES['file'])
            if msg is None:
                with open('file.csv', 'rb') as csv:
                    response = HttpResponse(csv.read())
                    response['content_type'] = 'application/csv'
                    response['Content-Disposition'] = 'attachment;filename=file.csv'
                    return response
            else:
                context = {}
                return render(request, 'app/download.html', context)

    context = {
        'form' : json_form ,
        'file_form' : file_form,
        'output' : csv
    }

    return render(request, 'app/index.html', context)