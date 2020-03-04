from django.apps import AppConfig
from django.apps import apps

class BioinformaticsappConfig(AppConfig):
    name = 'bioinformaticsapp'

INSTALLED_APPS=[
    'bioinformatics.apps.BioinformaticsappConfig'
]
