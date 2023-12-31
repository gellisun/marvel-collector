# Generated by Django 4.2.3 on 2023-08-02 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.CharField(choices=[(1, 'Poor'), (2, 'Alright'), (3, 'Good'), (4, 'Very Good'), (5, 'Amazing')], default=1, max_length=1)),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.comic')),
            ],
        ),
    ]
