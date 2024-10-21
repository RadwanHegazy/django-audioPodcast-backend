from django.contrib import admin
from .models import Stage

@admin.register(Stage)
class StagePanel(admin.ModelAdmin) : 
    list_display = ['title','owner','id']