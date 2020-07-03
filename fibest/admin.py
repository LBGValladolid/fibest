from django.contrib import admin

from .models.company import Company, Magazine, Stand, Forum
from .models.cv import CV

admin.site.register(CV)


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
    list_display = ('name', 'uploaded')
    list_editable = ('uploaded',)
    list_filter = ('disclaimer', 'assembly_service', 'uploaded')
    ordering = ('name', 'uploaded')

    inlines = [
        ForumAdmin,
        MagazineAdmin,
        StandAdmin

    ]
