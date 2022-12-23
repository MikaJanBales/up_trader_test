# Generated by Django 4.1.4 on 2022-12-27 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('explicit_url', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('named_url', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menuitem')),
            ],
        ),
    ]
