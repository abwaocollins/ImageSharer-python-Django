from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.template import context
from .models import Post, User
from django.views.generic import TemplateView,DetailView, FormView
from .forms import PostForm,RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login')
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts']= Post.objects.all().order_by('-id')
        return context
# @login_required(login_url='login')
class PostDetailView(DetailView):

    template_name = 'detail.html'
    model = Post
# @login_required(login_url='login')
class PostFormView(FormView):
    template_name = 'inputPost.html'
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request

        return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):

        new_object= Post.objects.create(
            title = form.cleaned_data['title'],
            description = form.cleaned_data['description'],
            author = form.cleaned_data['author'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS,'Your Post was successful')

        return super().form_valid(form)

def registerFormView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            user = User.objects.create_user(username,email,password1)

            login(request,user)

            messages.success(request,'account was created for ',user)
            
            return redirect('/login')

    context = {'form':form}
    return render(request,'register.html',context)

def loginFormView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/')

            else:
                messages.info(request, 'Username OR password is incorrect')

    context = { 'form': form}

    return render(request,'login.html',context)

def logoutView(request):
    logout(request)
    return redirect('/login')
# @login_required(login_url='login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect("/")

    context = { 'post': post}

    return render(request,'delete.html',context)




