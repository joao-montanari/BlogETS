# Generated by Django 4.1 on 2022-09-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_postagem_conteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostas',
            name='resposta',
            field=models.TextField(max_length=1000),
        ),
    ]
