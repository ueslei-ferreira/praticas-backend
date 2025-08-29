from django.contrib import admin
from .models import Artigos, Tag, ArtigoTag

admin.site.register(Artigos)
admin.site.register(Tag)
admin.site.register(ArtigoTag)
