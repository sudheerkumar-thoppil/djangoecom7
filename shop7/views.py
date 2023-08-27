from django.shortcuts import render, HttpResponse
from .models import Product,Category

# Create your views here.
def index(request):
    category = Category.objects.all()
    products=Product.objects.all()
    category_id=request.GET.get('category')
    # data={
    #     'category':category,
    #     'products':products

    # }
    if category_id:
        products=Product.objects.filter(category=category_id)
        return render(request,'categoryview.html',{{'products':products}})
    else:
        return render(request,'index.html',{'products':products,'category':category})
        # return render(request,'index.html',{'data':data})
       

def categoryview(category_id):
    # category=Product.objects.filter(category=category_id,).get(category_id)
    category=Category.objects.get(pk=category_id)
    category =Product.get.all_products_by_category_id(category_id)
    return render(category_id,'categoryview.html',{{'category':category}})