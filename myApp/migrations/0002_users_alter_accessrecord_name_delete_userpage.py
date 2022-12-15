# Generated by Django 4.1.4 on 2022-12-15 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('age', models.IntegerField(max_length=264)),
                ('url', models.URLField(unique=True)),
                ('userKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.inventory')),
            ],
        ),
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.users'),
        ),
        migrations.DeleteModel(
            name='UserPage',
        ),
    ]