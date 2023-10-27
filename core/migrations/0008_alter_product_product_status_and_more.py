# Generated by Django 4.2.4 on 2023-10-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_product_tags_alter_cartorder_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('published', 'Published'), ('disabled', 'Disabled'), ('draft', 'Draft'), ('in_review', 'in_Review'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (3, '⭐⭐⭐☆☆'), (2, '⭐⭐☆☆☆'), (1, '⭐☆☆☆☆'), (5, '⭐⭐⭐⭐⭐')], default=None),
        ),
    ]
