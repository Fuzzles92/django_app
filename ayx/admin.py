from django.contrib import admin
from .models import Collection, Workflow, DecomRequest

admin.site.register(Collection)
admin.site.register(Workflow)
admin.site.register(DecomRequest)