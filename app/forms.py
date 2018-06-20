from django.forms import Form, Textarea, CharField, FileField

class JsonForm(Form):
    json = CharField(widget=Textarea(attrs={'class':"form-control", 'id':"json"}))

    def __init__(self, *args, **kwargs):
        super(JsonForm, self).__init__(*args, **kwargs)
        self.fields['json'].label = False

class UploadFileForm(Form):
    file = FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].label = False