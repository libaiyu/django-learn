
from django import forms
from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        '''设置Meta'''
        model = Comment #设置表单form关联的模型model
        fields = ('username','content') #设置在模板中渲染的字段
