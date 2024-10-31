# Generated by Django 5.1.2 on 2024-10-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_menu_dia_remove_categorias_bebida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='Sin Categoría', max_length=60),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado'), ('entregado', 'Entregado')], max_length=20),
        ),
    ]
