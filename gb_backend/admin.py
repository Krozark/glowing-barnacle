from django.apps import apps
from django.contrib import admin

# all other models
for model in apps.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
