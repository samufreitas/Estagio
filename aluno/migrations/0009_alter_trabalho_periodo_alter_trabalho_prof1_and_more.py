# Generated by Django 4.2.3 on 2023-08-08 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_delete_trabalho'),
        ('aluno', '0008_remove_trabalho_autor_remove_trabalho_banca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='professor.periododisc'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='prof1',
            field=models.CharField(max_length=60, verbose_name='Professor1'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='prof2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Professor2'),
        ),
    ]
