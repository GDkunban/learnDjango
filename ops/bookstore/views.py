from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

# 将获取到的数据返回 'book_list.html'
def list_books(request):
    # 从模型中取数据
    books = models.Book.objects.all()
    print(books)
    return render(request, 'book_list.html', locals())

# 增加新书功能
def new_book(request):
    # 当请求为 GET 请求，返回一个html界面让用户填写信息
    if request.method == 'GET':
        return render(request, 'new_book.html')
    # 当请求为 POST 请求，将数据提交至数据库；并返回成功界面
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', '')
        market_price = request.POST.get('market_price', '')
        abook = models.Book.objects.create(
            title = title,
            pub = pub,
            price = price,
            market_price = market_price,
        )
        return render(request, 'add_success.html', locals())

# 通过获取用户修改的表数据id，对数据进行修改
def update(request, num):
    if request.method == 'GET':
        abook = models.Book.objects.get(id = num)
        print(abook.id, abook.title, abook.pub, abook.price, abook.market_price)
        return render(request, 'update.html', locals())
    if request.method == 'POST':
        market_price = request.POST.get('market_price', '')
        abook = models.Book.objects.get(id = num)
        abook.market_price = market_price
        abook.save()
    return HttpResponse("修改了表中的第 %s 条数据" % num)

def delete(request, num):
    abook = models.Book.objects.get(id = num)
    abook.delete()
    return HttpResponseRedirect('/bookstore')