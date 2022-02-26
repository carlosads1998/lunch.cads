# Generated by Django 2.2.9 on 2022-02-26 18:18

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nomei', models.CharField(max_length=120)),
                ('descricao', models.TextField(max_length=350)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=api.models.upload_image_comida)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente', models.CharField(max_length=100)),
                ('quan', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=1)),
                ('pag', models.CharField(choices=[('PIX', 'PIX'), ('CC', 'CARTÃO_CREDITO'), ('CD', 'CARTAO_DEBITO'), ('DINHEIRO', 'DINHEIRO')], max_length=9)),
                ('ped_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
            options={
                'verbose_name': 'PEDIDO',
            },
        ),
        migrations.CreateModel(
            name='entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('ENTREGUE', 'ENTREGUE'), ('PREPARO', 'PREPARO')], max_length=8)),
                ('identi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pedido')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]