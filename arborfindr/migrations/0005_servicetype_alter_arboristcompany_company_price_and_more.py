# Generated by Django 4.2.16 on 2024-12-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arborfindr', '0004_alter_arboristreview_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='arboristcompany',
            name='company_price',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='ServicesType',
        ),
        migrations.AddField(
            model_name='arboristcompany',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='companies', to='arborfindr.servicetype'),
        ),
    ]