from django.contrib import admin
from MyflixApp.models import Myflix, Genero

# class listandoFilmes(admin.ModelAdmin):
#     list_display = ('id', 'nome_filme', 'categoria', 'publicada')
#     list_display_links = ('id','nome_filme','categoria')
#     search_fields = ('nome_filme',)
#     list_filter = ('categoria',)
#     list_editable = ('publicada',)
#     list_per_page = 10


admin.site.register(Myflix)
admin.site.register(Genero)




