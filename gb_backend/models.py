"""
This file contain all the database representations of the objects
"""
from django.core.files import File
from django.db import models

from glowing_barnacle.images import improve_image_filepath


class UserImage(models.Model):
    original = models.ImageField(null=False, upload_to="original/")
    processed = models.ImageField(null=True, upload_to="processed/")

    def process_original(self):
        processed_filepath = improve_image_filepath(self.original.path)
        with File(open(processed_filepath, "rb")) as f:
            self.processed.save(
                self.original.name,
                f
            )

    def __str__(self):
        return self.original.url

