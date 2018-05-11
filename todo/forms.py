from django import forms

class TodoForm(forms.Form):
    text=forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={'class':'','placeholder': 'Enter todo','area-label':'Todo','area-describedby':'add-btn'}
    ))
