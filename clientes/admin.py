from django.contrib import admin
from .models import Person, Document


admin.site.register(Person)
admin.site.register(Document)