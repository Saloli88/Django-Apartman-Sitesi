# Generated by Django 4.1.4 on 2022-12-16 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_content_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]