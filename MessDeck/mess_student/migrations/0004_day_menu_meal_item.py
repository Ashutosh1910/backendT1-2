# Generated by Django 4.2.7 on 2023-11-23 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mess_student', '0003_remove_student_profile_mess_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=10)),
                ('of_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess_student.day_menu')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_rating_value', models.PositiveIntegerField(default=0, max_length=1)),
                ('item_avg_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('item_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess_student.meal')),
                ('item_rating', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
