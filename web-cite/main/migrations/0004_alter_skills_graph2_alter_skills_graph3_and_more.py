# Generated by Django 5.0.1 on 2024-01-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_skills_graph2_skills_graph3_skills_graph4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='graph2',
            field=models.ImageField(default='', upload_to='skills', verbose_name='График 2'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='graph3',
            field=models.ImageField(default='', upload_to='skills', verbose_name='График 3'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='graph4',
            field=models.ImageField(default='', upload_to='skills', verbose_name='График 4'),
        ),
    ]