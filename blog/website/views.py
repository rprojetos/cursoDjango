from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = [
        'Django',
        'Python',
        'Git',
        'Html',
        'Banco de dados',
        'Linux',
        'Nginx',
        'Uwsgi',
        'Systemctl'
    ]

    # list_posts = Post.objects.filter()
    list_posts = Post.objects.all()

    data = {
        'name':'Curso de DJango 3', 
        'lista_tecnologias': lista,
        'posts': list_posts
        }

    return render(request, 'index.html', data)
