from django import forms  
from APP.models import Movies
class MoviesForm(forms.ModelForm):  
    class Meta:  
        model = Movies  
        fields = "__all__"  