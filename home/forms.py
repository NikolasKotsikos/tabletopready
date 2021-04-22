from django import forms

QUERIES = (
    ('', 'Select Option'),
    ('How does Tabletop-READY work', 'How does Tabletop-READY work'),
    ('Order and shipping times', 'Order and shipping times'),
    ('I want a miniature added to the shop', 'I want a miniature added to the shop'),
    ('Something else', 'Something else'),
)


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full Name', max_length=100,
                                   widget=forms.TextInput())
    contact_email = forms.EmailField(label='Email Address',
                                     widget=forms.TextInput())
    query = forms.ChoiceField(label='What does your question relate to?',
                              choices=QUERIES)
    message = forms.CharField(label='What is your message?',
                              widget=forms.Textarea(
                                  attrs={'style': 'height:6em'}))
