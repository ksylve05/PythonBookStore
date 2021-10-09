# Generated by Django 3.2.7 on 2021-10-06 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20211006_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='quanity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='bookId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.book'),
        ),
        migrations.AlterField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]