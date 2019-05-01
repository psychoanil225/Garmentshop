from django import forms

class Contactform(forms.Form):
    contact_name= forms.CharField(label='Enter your name:', required=True)
    contact_emial= forms.EmailField(label='Enter Email Id:', required=True)
    contact_phone= forms.IntegerField(label='Enter mobile no:', required=True)
    content= forms.CharField(label='Enter your Message', required=True, widget= forms.Textarea)