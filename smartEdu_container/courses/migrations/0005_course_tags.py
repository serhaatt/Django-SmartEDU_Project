# Generated by Django 5.0.6 on 2024-07-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]