from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import POST

class PostForm(ModelForm):
    class Meta:
        model = POST 
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input-field'})