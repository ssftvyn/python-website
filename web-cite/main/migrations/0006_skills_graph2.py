# Generated by Django 5.0.1 on 2024-01-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_skills_graph2_remove_skills_graph3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='graph2',
            field=models.ImageField(default=None, null=True, upload_to='skills', verbose_name='График 2'),
        ),
    ]