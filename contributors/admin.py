from django.contrib import admin
from contributors.models import Contributor

class ContributorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contributor, ContributorAdmin)