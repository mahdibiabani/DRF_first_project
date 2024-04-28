from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Count, Min, Max, Value, Func, ExpressionWrapper, DecimalField, Prefetch
from .models import Category, Product, Customer, OrderItem, Order, Comment
from django.db import connection
def show_data(request):
    # queryset = Product.objects.filter(category__id=1)
    # queryset = Product.objects.filter(name__icontains='em', inventory__gt=50, datetime_created__year=2024 )
    # return render(request, 'hello.html', {'products': list(queryset)})
    # queryset_justin = Customer.objects.filter(first_name__icontains='j')
    # queryset = Order.objects.filter(customer__in=queryset_justin)
    # queryset = Product.objects.filter(~Q(inventory__lt=50) | Q(inventory__gt=90))
    # queryset = OrderItem.objects.filter(product__id=F('quantity'))
    # queryset = Product.objects.all()[10:15]
    # queryset = Product.objects.filter(inventory__gt=90).order_by('unit_price').reverse()
    # queryset = Product.objects.filter(inventory__gt=90).earliest('unit_price')
    # queryset = Product.objects.filter(inventory__gt=90).latest('unit_price')
    # queryset = Product.objects.order_by('-inventory').values('name', 'inventory')
    # .distinct() حذف تکراری ها
    # .values() داده ها را به صورت دیکشنری نمایش میدهد
    # .values_list() به صورت تاپل نمایش میدهد
    # queryset = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct())
    # queryset = Product.objects.only('id', 'name', 'inventory')
    # defer() همه چیزبه جز
    #select_related() برای فارینکی ها استفاده میشود
    # queryset = OrderItem.objects.select_related('product').all()
    # queryset = Product.objects.prefetch_related('order_items').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('items__product').all()
    # queryset = Product.objects.aggregate(avg=Avg('unit_price'), count=Count('id'),max_inv=Max('inventory'))
    # annotate() برای اضافه کردن یک فیلد به دیتابیس در کوئری ها
    # orders = OrderItem.objects.select_related('product').values('product_id').distinct()
    # queryset = orders.filter(product__datetime_created__year=2024)
    # queryset = OrderItem.objects.annotate(total=F('quantity') * F('unit_price')).all()
    # queryset = Customer.objects.annotate(fullname=Func(F('first_name'), Value(' '),F('last_name'), function='CONCAT')).all
    # queryset = Customer.objects.annotate(orders_number=Count('orders'))
    # queryset = OrderItem.objects.annotate(total_price=ExpressionWrapper(F('unit_price')* 0.95, output_field=DecimalField()))
    #expressionWrapper برای انجام عملیت روی یک فیلد مانند مثال بالا می باشد
    # queryset = Comment.objects.get_approved() تغییر منیجر
    # queryset = Comment.Approved.all()
    # queryset = Order.objects.get_by_status(status=Order.ORDER_STATUS_UNPAID)
    # print(queryset)
    # Comment.objects.create(
    #     name = 'mahdi',
    #     body = 'i love django framework',
    #     product_id = 1,

    # )
    #این روش برای ایجاد یک object مناسب تر است

    # product = Product.objects.get(id=1)

    # new_comment = Comment()
    # new_comment.name = 'mahdi'
    # new_comment.body = 'i love django framework'
    # new_comment.product= product
    # new_comment.save()


    #آپدیت کرن یک object
    # category = Category(pk=100)
    # category.title = 'Cars'
    # category.description = 'i dont know what to say'
    # category.top_product_id = 3
    # category.save()

    #روش دوم
    # Category.objects.filter(pk=98).update(title='AB')
    #پاک کردن
    #Category.objects.filter(pk=97).delete()
    #یا
    #cat = Category(pk=98)
    #cat.delete()
    
    #برای اجرای همزمان چند کد از transaction استفاده می شود
    # with transaction.atomic():
    #یا
    # @transaction.atomic()

    #اجرای sql خام
    # cursor = connection.cursor()

    # cursor.execute('# SQL code')
    # cursor.close()

    #اجرای یک کد نوشته شده در sql
    # cursor.callproc('proc_name', ورودی ها)

    queryset = Order.objects.prefetch_related(

        Prefetch(
            'items',
            queryset=OrderItem.objects.select_related('product')

        )
    ).annotate(
        item_count=Count('items')
        )  

    for order in queryset:

        for order_item in order.items.all():
         print(order_item.product.name)  
    return render(request, 'hello.html')
    
    # less than :  lt
    # greater than: gt
    # greater than or equal to :  gte
    # less than or equal to : lte
    # name__contains='hello'
    # name__icontains='hello'    به بزرگ و کوچکی حروف حساس نیست
    # queryset = Customer.objects.filter(birth_date__isnull=False)
    # return render(request, 'hello.html', {'customers':list(queryset)})
    # queryset = Product.objects.filter(datetime_cretated__year=2021)