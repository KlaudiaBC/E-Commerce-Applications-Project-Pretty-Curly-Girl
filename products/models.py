from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=254)
    extra_info = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    volume = models.IntegerField(null=False, blank=True, default="0")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True, default=None)
    sale = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Define the Review model
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_reviews"
    )
    author = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Set the order of displaying the posts
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.author}"
