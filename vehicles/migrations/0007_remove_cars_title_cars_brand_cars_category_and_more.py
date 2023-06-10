# Generated by Django 4.2.2 on 2023-06-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_alter_cars_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='title',
        ),
        migrations.AddField(
            model_name='cars',
            name='brand',
            field=models.CharField(default='Toyota', max_length=20, verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='cars',
            name='category',
            field=models.CharField(choices=[('car', 'Auto'), ('pickup', 'Camioneta'), ('comecial', 'Comercial'), ('suv', 'SUV'), ('cross', 'CrossOver')], default='car', max_length=30, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='cars',
            name='model',
            field=models.CharField(max_length=35, null=True, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='cars', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]
