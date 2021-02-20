from django.forms import ModelForm

from .models import User


class SignIn(ModelForm):

    # specifiy the the name of the model to use
    class Meta:
        model = User
        # specify all the fields to render
        fields = "__all__"
