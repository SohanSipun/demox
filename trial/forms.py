from .models import StudentModel
from django import forms
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})

        }
