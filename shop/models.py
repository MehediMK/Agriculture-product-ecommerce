from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=20, blank=False)
    category_image = models.ImageField(upload_to='category_image')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


POST_TYPE = (
    ("FS", "For Sale"),
    ("FB", "For Buy"),
)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=250, blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image', blank=False)
    product_description = models.TextField(max_length=600, blank=False)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, blank=True)
    post_type = models.CharField(max_length=20, choices=POST_TYPE)
    updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)


class BeatItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reply = models.CharField(max_length=500, blank=False)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply


class Carousel(models.Model):
    Catitle = models.CharField(
        max_length=100, verbose_name='Title', blank=True)
    CaSubTitle = models.CharField(
        max_length=150, verbose_name='Subtitle', blank=True)
    CaImage = models.ImageField(
        upload_to='carouselImage', verbose_name='Image', blank=False)
    offer_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Catitle if self.Catitle else "Carousel"


class OrderPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    total_amout = models.DecimalField(max_digits=6, decimal_places=2)
    TrxID = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

    @property
    def total_price(self):
        return self.quantity*self.total_amout

    @staticmethod
    def get_orders_by_customer(user):
        return OrderPlace.objects.filter(user=user).order_by('-id')
