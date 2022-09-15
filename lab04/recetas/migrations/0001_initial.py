# Generated by Django 4.1.1 on 2022-09-14 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('ingredientes', models.CharField(help_text='Redacta los Ingredientes', max_length=9999)),
                ('preparaicon', models.TextField()),
                ('tiempo_registro', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(help_text='Tu comentario', verbose_name='Comentario')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.receta')),
            ],
        ),
    ]
