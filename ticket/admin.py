from django.contrib import admin

# Register your models here.
from .models import IssueType,Ticket


class EmptyAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):

    # Return empty perms dict thus hiding the model from admin index.

        return {}



admin.site.register(IssueType)

admin.site.register(Ticket)