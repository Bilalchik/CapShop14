from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(upload_to='media/product/detail_photo')


class Product(models.Model):
    main_cover = models.ImageField(
        upload_to='media/product/cover'
    )
    title = models.CharField(
        max_length=123
    )
    description = models.TextField()
    brands = models.ManyToManyField(Brand)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'XS'),
            (2, 'S'),
            (3, 'M'),
            (4, 'L'),
            (5, 'XL'),
            (6, 'XXL')
        )
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT
    )
    old_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        blank=True,
        null=True
    )
    actual_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00
    )
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title


class Storage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'В наличии'),
            (2, 'Скоро в наличии'),
            (3, 'Нет в наличии'),
        )
    )

    def __str__(self):
        return str(self.product)






