from django import forms
from .widgets import CustomClearableFileInput
from .models import Style


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Style
        fields = '__all__'

    image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        picture = Style.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

