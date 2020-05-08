# Generated by Django 3.0.5 on 2020-04-30 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=368)),
                ('image', models.URLField(max_length=368)),
                ('nutriscore', models.CharField(max_length=1)),
                ('energy', models.DecimalField(decimal_places=4, max_digits=9, null=True)),
                ('proteins', models.DecimalField(decimal_places=4, max_digits=7, null=True)),
                ('fat', models.DecimalField(decimal_places=4, max_digits=7, null=True)),
                ('saturated_fat', models.DecimalField(decimal_places=4, max_digits=7, null=True)),
                ('sugar', models.DecimalField(decimal_places=4, max_digits=7, null=True)),
                ('salt', models.DecimalField(decimal_places=4, max_digits=7, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
        ),
    ]
