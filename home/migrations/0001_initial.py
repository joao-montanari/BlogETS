# Generated by Django 4.1 on 2022-09-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('sub_titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('conteudo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('resposta', models.CharField(max_length=1000)),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.postagem')),
            ],
        ),
    ]