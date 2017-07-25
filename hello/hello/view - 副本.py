

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("hello ! \n 哈哈，终于开始了。　")
