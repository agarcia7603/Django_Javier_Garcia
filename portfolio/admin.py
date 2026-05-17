from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Portfolio, PortfolioAdmin)