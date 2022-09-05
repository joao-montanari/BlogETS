from django.contrib import admin
from home.models import Postagem
from home.models import Respostas

# Register your models here.
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'autor')
    list_editable = ('curso',)
    list_display_links = ('titulo',)
    list_per_page = 10

class RespostasAdmin(admin.ModelAdmin):
    list_display = ('autor',)
    list_display_links = ('autor',)
    list_per_page = 10

admin.site.register(Respostas, RespostasAdmin)
admin.site.register(Postagem, PostagemAdmin)