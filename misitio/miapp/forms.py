from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Marca', 'Modelo','Color','Precio','Año','Num_Puertas','Descripción','Precio')