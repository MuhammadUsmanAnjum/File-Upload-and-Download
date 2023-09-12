from django.forms import ModelForm
from .models import FileUpload

# Create the form class.
class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'description', 'file']