from django import forms

class uploadform(forms.Form):
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    title = forms.CharField(max_length=100)
    filepath = forms.ImageField( max_length=None, allow_empty_file=False)
    desc = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
   