from django.contrib import admin

from .models.company import Company
from .models.cv import CV

admin.site.register(Company)
admin.site.register(CV)