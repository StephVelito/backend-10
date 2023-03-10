# Generated by Django 4.1.7 on 2023-02-23 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petsplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoletasPagoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45)),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True, null=True)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='CitasCategoriasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.categoriasmodel')),
            ],
            options={
                'db_table': 'cita_categorias',
            },
        ),
        migrations.CreateModel(
            name='CitasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('estado', models.BooleanField(default=True, null=True)),
            ],
            options={
                'db_table': 'cita',
            },
        ),
        migrations.CreateModel(
            name='ClientesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('dni', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='DetallesOrdenModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('cita_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.citasmodel')),
            ],
            options={
                'db_table': 'detalles_orden',
            },
        ),
        migrations.CreateModel(
            name='OrdenesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45)),
                ('observacion', models.CharField(max_length=100, null=True)),
                ('estado', models.BooleanField(default=True, null=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.clientesmodel')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ordenes',
            },
        ),
        migrations.CreateModel(
            name='PagosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('numero_pago', models.IntegerField()),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.ordenesmodel')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
        migrations.DeleteModel(
            name='ProductosModel',
        ),
        migrations.AddField(
            model_name='detallesordenmodel',
            name='orden_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.ordenesmodel'),
        ),
        migrations.AddField(
            model_name='citascategoriasmodel',
            name='cita_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.citasmodel'),
        ),
        migrations.AddField(
            model_name='boletaspagomodel',
            name='pago_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsplace.pagosmodel'),
        ),
    ]
