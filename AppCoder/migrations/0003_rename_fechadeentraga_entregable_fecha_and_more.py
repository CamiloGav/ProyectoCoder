# Generated by Django 4.1.7 on 2023-03-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_curso_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='fechaDeEntraga',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
