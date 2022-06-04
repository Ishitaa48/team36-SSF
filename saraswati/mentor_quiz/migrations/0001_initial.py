# Generated by Django 4.0.5 on 2022-06-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questions', models.TextField(max_length=500)),
                ('opt1', models.CharField(max_length=100)),
                ('opt2', models.CharField(max_length=100)),
                ('opt3', models.CharField(max_length=100)),
                ('opt4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('Taxonomy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NineTen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(max_length=500)),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op4', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('Taxonomy', models.CharField(max_length=100)),
            ],
        ),
    ]