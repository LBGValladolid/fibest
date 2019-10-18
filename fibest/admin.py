from django.contrib import admin

from .models.company import Company, Magazine, Stand, Forum
from .models.cv import CV

admin.site.register(Company)
admin.site.register(CV)
admin.site.register(Magazine)
admin.site.register(Stand)
admin.site.register(Forum)