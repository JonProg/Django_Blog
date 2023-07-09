from django.urls import path
from blog.views import PostListView, CreatedByListView,\
CategoryListView, TagListView, SearchListView, PageDatailView
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('page/<slug:slug>/', PageDatailView.as_view(), name='page'),
    path('created_by/<int:author_id>/', CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
]