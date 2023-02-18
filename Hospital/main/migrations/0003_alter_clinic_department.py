# Generated by Django 4.1.7 on 2023-02-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_clinic_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('HC', 'Heart Center'), ('NC', 'Neuroscience Center'), ('OBC', 'Obesity Center'), ('EC', 'Eye Center'), ('ORC', 'Orthopedic Center'), ('PC', 'Pediatric Center')], default='HC', max_length=3),
        ),
    ]
