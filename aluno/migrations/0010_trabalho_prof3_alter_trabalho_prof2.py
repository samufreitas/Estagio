# Generated by Django 4.2.3 on 2023-08-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0009_alter_trabalho_periodo_alter_trabalho_prof1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalho',
            name='prof3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Professor3'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='prof2',
            field=models.CharField(default=1, max_length=60, verbose_name='Professor2'),
            preserve_default=False,
        ),
    ]
