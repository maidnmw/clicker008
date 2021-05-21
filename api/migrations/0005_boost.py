# Generated by Django 3.1.7 on 2021-05-21 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_maincycle_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=10)),
                ('level', models.IntegerField(default=0)),
                ('main_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.maincycle')),
            ],
        ),
    ]
