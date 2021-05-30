from django import forms
from .models import Order, Device


class OrderForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'input_address'}))

    class Meta:
        model = Order
        fields = ('address',)


class OrderDocumentation(forms.ModelForm):

    image = forms.ImageField(required=False)
    specification = forms.FileField(required=False)

    class Meta:
        model = Order
        fields = ('image', 'spec_document')


class DeviceForm(forms.ModelForm):

    name = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'input_name'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '2', 'id': 'input_description'}))
    is_street = forms.BooleanField(required=False)
    is_room = forms.BooleanField(required=False)
    max_temp = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'input_max'}))
    min_temp = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'input_min'}))
    is_220 = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'input_220'}))
    requirements = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '5', 'id': 'input_requirements'}))
    is_private = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'input_private'}))

    class Meta:
        model = Device
        fields = ('name',
                  'description',
                  'is_street',
                  'is_room',
                  'max_temp',
                  'min_temp',
                  'is_220',
                  'requirements',
                  'is_private')
