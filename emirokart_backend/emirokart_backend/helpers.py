from django.apps import apps
from django.db import models

def get_dynamic_form_models():
    return {
        'customer':'customer.Customer',
        'product':'product.Product',
        'category':'category.Category',
    }

def get_dynamic_form_fields(model_instance):
    if not model_instance:
        return []
    
    fields = []
    for field in model_instance._meta.get_fields():
        if isinstance(field, models.Field):
            if field.auto_created or field.primary_key:
                continue
            fields.append(field.name)

    return fields 