from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import Group  # Import the Group model

# Function to register models with the admin site
def register_models(app_config, admin_site):
    for model_name in app_config.get_models():
        model = apps.get_model(app_config.label, model_name)
        if model not in admin_site._registry:
            admin_site.register(model)

# Register models from 'myapp' with the admin site
app_config = apps.get_app_config('myapp')
register_models(app_config, admin.site)

# Unregister the Group model if it's already registered
if Group in admin.site._registry:
    admin.site.unregister(Group)


