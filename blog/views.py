from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
def inicio(request):
 posts = Post.objects.all()

 
 return render(request, 'blog/index.html', {
  'posts': posts
 })

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {
    'post': post
    })

@login_required
def crear_post(request):
   if request.method == 'POST':
      form = PostForm(request.POST, request.FILES)

      if form.is_valid():
         post = form.save(commit=False)
         post.autor = request.user
         post.save()
         return redirect('inicio')

   else:
       form=PostForm()

   return render(request, 'blog/crear_post.html', {
       'form' : form
    })

@login_required
def editar_post (request, pk):
   post = get_object_or_404(Post, pk=pk)

   if post.autor != request.user:
       return redirect('inicio')
   if request.method == 'POST':
      form = PostForm(request.POST, request.FILES, instance=post)

      if form.is_valid():
          form.save()
          return redirect('detalle_post', pk=post.pk)

   else:
        form = PostForm(instance=post) 
   return render(request, 'blog/editar_post.html', {
        'form': form,
        'post': post
    })
# para no olvidar lo importante:

@login_required
def eliminar_post(request, pk):
    # esto busca el post al momento de entrar a la web al recibir el GET, va a largar un POST despues
    post = get_object_or_404(Post, pk=pk)

# si no es el autor te manda al inicio, si lo llego a cambiar lo voy a comentar para recordar
    if post.autor != request.user:
        return redirect('inicio')
# hay 2 metodos, post y get, usamos post para editar el post o eliminar o publicar
    if request.method == 'POST':
        post.delete()
        return redirect('inicio')
# si todo sale bien te deberia de llevar al html
    return render(request, 'blog/eliminar_post.html', {
        'post': post
    })

def registro (request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect ('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'blog/registro.html',{

   'form': form })

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')

    else:

        form = AuthenticationForm()

    return render(request, 'blog/login.html',{
        'form': form
    })

def logout_usuario(request):
    logout(request)
    return redirect ('inicio')