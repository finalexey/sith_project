from django.contrib import admin

from .models import Planet, Sith, Recruit
from recruit_polls.models import *


class SithAdmin(admin.ModelAdmin):

    list_display = ['name', 'planet']

    class Meta:
        model = Sith


class RecruitAdmin(admin.ModelAdmin):

    list_display = ['name', 'planet']

    class Meta:
        model = Sith


admin.site.register(Planet)
admin.site.register(Sith, SithAdmin)
admin.site.register(Recruit, RecruitAdmin)
