# Generated by Django 3.1.1 on 2020-09-26 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(blank=True, max_length=128, null=True)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('sell_price', models.DecimalField(blank=True, decimal_places=2, default=10.99, max_digits=100, null=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=200)),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='productimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop/images')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SubCategory', to='shop.subcategory'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('title', 'slug'), name='name of constraint'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'slug')},
        ),
    ]