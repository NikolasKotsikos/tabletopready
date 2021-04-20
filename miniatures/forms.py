from django import forms
from .models import Miniature, Army, GamingSystem


class MiniatureForm(forms.ModelForm):

    class Meta:
        model = Miniature
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        armies = Army.objects.all()
        gamesystems = GamingSystem.objects.all()
        armies_friendly_names = [(a.id, a.get_friendly_name()) for a in armies]
        gamesystems_friendly_names = [(gs.id, gs.get_friendly_name()) for gs in gamesystems]

        self.fields['army'].choices = armies_friendly_names
        self.fields['gamesys'].choices = gamesystems_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
