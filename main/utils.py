from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить пост', 'url_name': 'add_post'},
]

class DataMixin:
    paginate_by = 1
    def get_extra_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu 
        context['common_tags'] = Post.tags.most_common()
        return context