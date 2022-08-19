from django.urls import path
from .views import HomePageView,PostDetailView,PostFormView,registerFormView,loginFormView,logoutView,deletePost
from django.contrib.auth.decorators import login_required
app_name = 'feed'

urlpatterns = [
    path('',login_required(HomePageView.as_view(),login_url='/login'), name='index'),
    path('info/<int:pk>',login_required(PostDetailView.as_view(),login_url="/login"), name='detail'),
    path('delete/<int:pk>',login_required(deletePost,login_url="/login"), name='delete'),
    path('post/',login_required(PostFormView.as_view(), login_url="/login"),name='newPost'),
    path('register/',registerFormView,name='register'),
    path('login/',loginFormView,name='login'),
    path('logout/', logoutView, name="logout"),

]