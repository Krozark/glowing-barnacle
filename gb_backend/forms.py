"""
This file contain all the form of the project
"""

from django import forms


class UploadImageForm(forms.Form):
    """
    Simple form to get images
    """
    image = forms.ImageField()

    # class Meta:
    app_label = "bg_backend"
