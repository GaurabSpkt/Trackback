from django import forms
from .models import ItemLost
from .models import Contact

class Lost(forms.ModelForm):
     class Meta:
        model = ItemLost
        fields = ['title', 'description', 'phone_number', 'email', 'location', 'image', 'found']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter details like color, size, quantity, species'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'found': forms.CheckboxInput(),
        }
        labels = {
            'title': 'Item Name',
            'description': 'Description (Color, Size, Quantity, Species)',
            'phone_number': 'Contact Number',
            'email': 'Email Address',
            'location': 'Location',
            'image': 'Upload Image',
            'found': 'Found',
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
        label='Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        label='Email'
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Contact Number'}),
        label='Contact Number'
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'}),
        label='Message'
    )
