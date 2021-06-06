from django.contrib import admin
from .models import Post, Contatic

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'sub_title', 'title_subtitle', 'categories','approved'
        ]
    search_fields = ['title', 'sub_title']

    #filtrando o que será mostrado:
    def get_queryset(self, request):
        return Post.objects.all()
        #return Post.objects.filter(approved=True)

admin.site.register(Post, PostAdmin)
admin.site.register(Contatic)

