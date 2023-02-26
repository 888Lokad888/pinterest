from .models import *

unatheticated_menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить пост', 'url_name': 'add_post'},
]

authiticated_menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить пост', 'url_name': 'add_post'},
    {'title': 'Понравившееся', 'url_name': 'liked'}
]

class DataMixin:
    def get_extra_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context['menu'] = authiticated_menu 
        else:
            context['menu'] = unatheticated_menu 
        context['common_tags'] = Post.tags.most_common()
        return context