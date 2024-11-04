# Generated by Django 5.1.2 on 2024-11-01 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_admin', models.CharField(max_length=50)),
                ('apellido_admin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Categoria', models.CharField(default='Sin Categoría', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('Total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Canton', models.CharField(max_length=100)),
                ('Distrito', models.CharField(max_length=100)),
                ('Provincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_empleado', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=20)),
                ('Codigo_empleado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plato', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Postre', models.CharField(max_length=20)),
                ('Plato_Fuerte', models.CharField(max_length=80)),
                ('Bebida', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado'), ('entregado', 'Entregado')], max_length=20)),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Metodo_pago', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.CharField(max_length=25)),
                ('stock', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Promocion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Proveedor', models.CharField(max_length=20)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje_reseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.administrador')),
                ('Direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.direccion')),
                ('mensaje_reseña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.resena')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.direccion')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AddField(
            model_name='menu',
            name='Plato_Del_Dia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu_dia'),
        ),
        migrations.AddField(
            model_name='orden',
            name='Menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu'),
        ),
        migrations.AddField(
            model_name='detalles_orden',
            name='Orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orden'),
        ),
        migrations.AddField(
            model_name='detalles_orden',
            name='Pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pago'),
        ),
        migrations.AddField(
            model_name='menu',
            name='Promocion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.promociones'),
        ),
        migrations.AddField(
            model_name='producto',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedor'),
        ),
        migrations.AddField(
            model_name='detalles_orden',
            name='Restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurante'),
        ),
        migrations.AddField(
            model_name='orden',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario'),
        ),
    ]
