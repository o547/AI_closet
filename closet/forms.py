from django.forms import ModelForm
from .models import garment,coordinate

class GarmentForm(ModelForm):
    class Meta:
        model=garment
        fields=["name","color","type"]

class CoordinateForm(ModelForm):
    class Meta:
        model=coordinate
        fields=["temperature","tops","bottoms","outer","inner","accessory","additional1","additional2"]
