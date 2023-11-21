from django import forms
from .models import StudentInfo, Division, FavoriteSub
from django.forms import TextInput, EmailInput

class DivisionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class FavoriteSubMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class StudentModelForm(forms.ModelForm):
    division_set = DivisionModelChoiceField(
        queryset = Division.objects.all(),
        required = True,
        widget = forms.Select(attrs= {
            'class' : 'form-select',
        })
    )
    favorite_subject = FavoriteSubMultipleChoiceField(
        queryset = FavoriteSub.objects.all(),
        required = True,
        widget = forms.CheckboxSelectMultiple(attrs= {
            'class' : '',
        })
    )

    class Meta:
        model = StudentInfo
        fields = ['name','email','psu_id','division_set','favorite_subject']
        widgets = {
            'name' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'John Doe',
            }),
            'email' : EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'example@gmail.com',
            }),
            'psu_id' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'PSU PASSPORT',
            }),
        }