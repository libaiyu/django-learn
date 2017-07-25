
from django.views.generic import ListView, DetailView
import markdown2
from blog.models import Article, Category, Tag


class CategoryView(ListView):
    template_name = 'blog/index.html'  #和首页一样
    context_object_name = 'article_list'  #要的就是文章列表，也是一样

    #重写get_queryset方法，从已发布的文章中按分类筛选
    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['category_id'],status='published')
        return article_list

    #重写，返回分类和标签列表
    def get_context_data(self,**kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('category')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag')
        return super(CategoryView,self).get_context_data(**kwargs)

#和CategoryView完全一样        
class TagView(ListView):
    template_name = 'blog/index.html'  #和首页一样
    context_object_name = 'article_list'  #要的就是文章列表，也是一样

    #重写get_queryset方法，从已发布的文章中按标签筛选
    def get_queryset(self):
        article_list = Article.objects.filter(tag=self.kwargs['tag_id'],status='published')
        return article_list

    #重写，返回分类和标签列表
    def get_context_data(self,**kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('category')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag')
        return super(TagView,self).get_context_data(**kwargs)


class ArticleView(DetailView):
    model = Article   #不指定queryset就要指定model
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'  #URLconf中主键的关键字参数的名称

    #重写，把正文转换成markdown格式。该方法使用pk_url_kwarg参数查找对象
    def get_object(self):
        obj = super(ArticleView,self).get_object()
        obj.text = markdown2.markdown(obj.text)
        return obj


#这类视图与ListView通用视图功能一致，所以继承通用视图完成
class IndexView(ListView):
    template_name = 'blog/index.html'
    #告诉视图对这个页面进行渲染
    context_object_name = 'article_list'
    #给上下文变量取名，和模板中的那个变量一致

    #重写get_queryset方法，只显示已发布的文章
    def get_queryset(self):
        article_list = Article.objects.filter(status='published')
        return article_list

    #重写ListView下的get_context_data()方法，返回分类和标签列表
    def get_context_data(self,**kwargs):
        #category_list与html中一致，category与Category模型中的category一致
        kwargs['category_list'] = Category.objects.all().order_by('category')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag')
        return super(IndexView,self).get_context_data(**kwargs)

    
'''

# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from blog.models import Article


#这类视图与ListView通用视图功能一致，所以继承通用视图完成
class IndexView(ListView):
    template_name = 'blog/index.html'
    #告诉视图对这个页面进行渲染
    context_object_name = 'article_list'
    #给上下文变量取名，和模板中的那个变量一致

    #重写get_queryset方法，只显示已发布的文章
    def get_queryset(self):
        article_list = Article.objects.filter(status='published')
        return article_list
'''
