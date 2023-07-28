# Generated by Django 4.2.3 on 2023-07-28 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aluno', '0005_rename_user_periodo_plano_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plano',
            name='user_orientador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos_orientados', to=settings.AUTH_USER_MODEL),
        ),
    ]