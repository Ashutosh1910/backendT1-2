# Generated by Django 4.2.7 on 2023-12-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_student', '0019_alter_item_item_name_alter_meal_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=20),
        ),
    ]