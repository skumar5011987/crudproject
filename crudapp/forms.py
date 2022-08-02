from django.core import validators
from django import forms
from .models import Employee

ROLE=(
    ('CEO','Chief Executive Officer'),
    ('CMO','Chief Marketing Officer'),
    ('CTO','Chief Marketing Officer'),
    ('OM','Operations Manager'),
    ('PM','Product Manager'),
    ('CSSM','Customer Service & Support Manager'),
    ('BDM','Business Development Manager'),
    ('BA','Business analyst'),
    ('NE','Network engineer'),
    ('SE','Software engineer'),
    ('SSE','Senior Software engineer')
)

class RegisterationForm(forms.ModelForm):
    
    class Meta:
        model= Employee
        fields = ['name','role','email']  
        # fields = '__all__'       
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control text-dark' ,'placeholder':'Enter name'}), 
            'role':forms.TextInput(attrs={'class':'form-control text-dark','placeholder':'Role'}),           
            'email':forms.EmailInput(attrs={'class':'form-control text-dark','placeholder':'Enter email'}),            
        }