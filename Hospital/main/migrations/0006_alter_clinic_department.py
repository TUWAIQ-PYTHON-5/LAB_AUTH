# Generated by Django 4.1.7 on 2023-02-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_clinic_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('Heart Center', 'Heart Center'), ('Neuroscience Center', 'Neuroscience Center'), ('Obesity Center', 'Obesity Center'), ('Eye Center', 'Eye Center'), ('Orthopedic Center', 'Orthopedic Center'), ('Pediatric Center', 'Pediatric Center')], default='', max_length=50),
        ),
    ]
