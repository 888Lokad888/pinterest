from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.db.models import Count
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .utils import *

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for: ip = x_forwarded_for.split(',')[0]
    else: ip = request.META.get('REMOTE_ADDR')
    return ip

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена :((()))')

class HomePage(DataMixin, ListView):
    model = Post 
    template_name = 'main/index.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Главная страница'
        if (self.kwargs.get('tag_slug', None) is not None) and (self.request.GET.get('search-queue', None) != ''):
            title = f'Поиск по тэгу: {self.kwargs["tag_slug"]}'
        extra_context = self.get_extra_context(title=title)
        
        last_input = self.request.GET.get('search-queue', None)
        if last_input:
            extra_context = self.get_extra_context(
                title = f'Поиск по тэгам: {", ".join(last_input.split())}' or 'Главная страница',
                last_input = last_input
                )
        return dict(list(context.items()) + list(extra_context.items()))
    
    def get_queryset(self):
        posts = Post.objects.filter(is_published=True)
        if 'search-queue' in self.request.GET:
            search = self.request.GET['search-queue'].split()
            if search:
                posts = posts.filter(tags__name__in=search).annotate(num_tags=Count('tags')).filter(num_tags__gte=len(search)).order_by('-time_create') 
        elif 'tag_slug' in self.kwargs:
            posts = posts.filter(tags__name=self.kwargs['tag_slug'])
        return posts

class ShowPost(DataMixin, DetailView):
    model = Post 
    template_name = 'main/show_post.html'
    slug_url_kwarg = 'post_uuid'
    slug_field = 'num'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #VIEWS
        ip = get_client_ip(self.request)
        if not IpModel.objects.filter(ip=ip).exists():
            IpModel.objects.create(ip=ip)
        kwargs['object'].views.add(IpModel.objects.get(ip=ip))

        #LIKES
        user = self.request.user.id

        if 'buttton' in self.request.GET:
            if kwargs['object'].likes.filter(id=user).exists():
                kwargs['object'].likes.remove(user)
            else:
                kwargs['object'].likes.add(user)
            
        if kwargs['object'].likes.filter(id=self.request.user.id).exists():
            liked = True
        else:
            liked = False

        extra_context = self.get_extra_context(
            title=', '.join(kwargs['object'].tags.slugs()),
            liked=liked
        )
        return dict(list(context.items()) + list(extra_context.items())) 

class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/add_post.html'

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.posted_by = self.request.user
        newpost.save()
        if newpost.author:
            form.cleaned_data['tags'].append(newpost.author)
        form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_extra_context(
            title='Добавление поста', 
            header='Добавление поста',
            button='Отправить',
        )
        return dict(list(context.items()) + list(extra_context.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_extra_context(
            title='Регистрация',
            header='Регистрация',
            button='Зарегестрироваться'
        )
        return dict(list(context.items()) + list(extra_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm 
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_extra_context(
            title='Авторизация',
            header='Авторизация',
            button='Войти'
        )
        return dict(list(context.items()) + list(extra_context.items()))
    
def profile(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='profile')
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form, 
        'profile_form': profile_form
    }

    return render(request, 'main/profile.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')