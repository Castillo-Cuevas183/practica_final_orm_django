# Generated by Django 5.1.2 on 2024-10-30 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('f_fabricacion', models.DateField()),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=12)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
    ]
