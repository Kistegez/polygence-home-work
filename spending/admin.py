from django.contrib import admin

from spending.models import Spending

class SpendingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Spending, SpendingAdmin)