from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title=models.CharField(max_length=120,null=False,blank=False)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=100)
    sale_price=models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    slug=models.SlugField(unique=True)
    create_date=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_date=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together=('title','slug')

class ProductImage(models.Model):
    product=models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/images',null=True,blank=True)
    featured=models.BooleanField(default=False)
    thumbnail=models.BooleanField(default=False)
    updated_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager,self).filter(active=True)
    def sizes(self):
        return self.all().filter(category='size')
    def colors(self):
        return self.all().filter(category='color')

VAR_CATEGORIES=(
    ('size','size'),
    ('color','color')
)
class Variation(models.Model):
    product=models.ForeignKey(Product,related_name='variations',on_delete=models.CASCADE)
    category=models.CharField(max_length=120,choices=VAR_CATEGORIES,default='size')
    title=models.CharField(max_length=120)
    image=models.ForeignKey(ProductImage,related_name='var_images',on_delete=models.CASCADE,null=True,blank=True)
    price=models.DecimalField(max_digits=100,decimal_places=2,null=True,blank=True)
    updated_date=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
    active=models.BooleanField(default=True)

    objects=VariationManager()

    def __str__(self):
        return self.title
