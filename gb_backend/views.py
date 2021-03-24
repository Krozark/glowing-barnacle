"""
This file contain all the views of the project
"""
import logging

from django.http import HttpResponse
from django.views.generic import (
    FormView
)

from .forms import UploadImageForm
from .models import UserImage

logger = logging.getLogger(__name__)


class UploadImageView(FormView):
    """
    View to manage a incomming image upload
    """
    form_class = UploadImageForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            image = request.FILES["image"]
            logging.debug("Image uploaded %s", image)
            ui = UserImage()
            ui.original.save(
                image._name,
                image.file
            )
            ui.process_original()
            ui.save()
            return HttpResponse(content=ui.processed.url)
        return HttpResponse(status=400)
