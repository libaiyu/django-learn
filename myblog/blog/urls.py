"""blog URL Configuration

"""

from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    # 使用简单的正则，匹配浏览器传回的article_id,'()'内就是要捕获的信息.
    url(r'^article/(?P<article_id>\d+)$',views.ArticleView.as_view(),name='article'),
    url(r'^category/(?P<category_id>\d+)$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<tag_id>\d+)$',views.TagView.as_view(),name='tag'),
    
]
