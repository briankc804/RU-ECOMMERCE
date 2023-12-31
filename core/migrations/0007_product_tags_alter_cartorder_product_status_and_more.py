# Generated by Django 4.2.4 on 2023-10-20 07:18

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('core', '0006_product_life_product_mfd_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('process', 'Processing'), ('shipped', 'Shipped')], default='processing', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('published', 'Published'), ('disabled', 'Disabled'), ('in_review', 'in_Review'), ('draft', 'Draft'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(3, '⭐⭐⭐☆☆'), (2, '⭐⭐☆☆☆'), (5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐☆'), (1, '⭐☆☆☆☆')], default=None),
        ),
    ]
