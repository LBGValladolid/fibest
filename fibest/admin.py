from django.contrib import admin

from .models.company import Company, Magazine, Stand, Forum
from .models.cv import CV

# admin.site.register(Company)
admin.site.register(CV)
admin.site.register(Magazine)
admin.site.register(Stand)

admin.site.register(Forum)


class ForumAdmin(admin.StackedInline):
    model = Forum
    extra = 0
    max_num = 1
    can_delete = False


class MagazineAdmin(admin.StackedInline):
    model = Magazine
    extra = 0
    max_num = 1
    can_delete = False


class StandAdmin(admin.StackedInline):
    model = Stand
    extra = 0
    max_num = 1
    can_delete = False


@admin.register(Company)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    list_filter = ('disclaimer', 'assembly_service')
    ordering = ('name',)

    inlines = [
        ForumAdmin,
        MagazineAdmin,
        StandAdmin

    ]
