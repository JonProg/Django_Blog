from django.urls import path
from blog.views import PostListView
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('search/', views.search, name='search'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('page/<slug:slug>/', views.page, name='page'),
    path('created_by/<int:author_id>/', views.created_by, name='created_by'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('tag/<slug:slug>/', views.tag, name='tag'),
]