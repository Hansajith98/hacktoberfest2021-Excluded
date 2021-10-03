from django import forms
from .models import Hotel


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ('fullname','email','contact','gender','roomtype','checkstatus','age','date_of_join','income','address','hotelImg')
        labels = {
            'fullname':'Full Name',
            'age':'Age',
            'email':'Email',
            'contact':'Contact',
            'gender':'Gender',
            'income':'Income',
            'address':'Address',
            'hotelImg':'Image'
        }

        widgets = {
        'fullname': forms.TextInput(),
        'email': forms.EmailInput(),
        'contact': forms.NumberInput(),
        'age': forms.NumberInput(),
        'date_of_join': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'address': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        'hotelImg': forms.FileInput()
        }

        
    def __init__(self, *args, **kwargs):
        super(HotelForm,self).__init__(*args, **kwargs)
        self.fields['roomtype'].empty_label = "Select"
