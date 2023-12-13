# Generated by Django 4.2.7 on 2023-12-12 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess_student', '0016_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal_attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_attended', models.PositiveIntegerField(default=0)),
                ('meal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mess_student.meal')),
            ],
        ),
    ]