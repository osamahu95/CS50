# Generated by Django 3.0.7 on 2021-07-19 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sampleposts', '0003_auto_20210719_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='sampleposts.User'),
        ),
    ]
