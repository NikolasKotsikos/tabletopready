from django import forms
from miniatures.widgets import CustomClearableFileInput
from gallery.models import GalleryItem


class GalleryItemForm(forms.ModelForm):

    class Meta:
        model = GalleryItem
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
