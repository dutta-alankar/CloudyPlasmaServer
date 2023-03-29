# Generated by Django 4.1.7 on 2023-03-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0002_alter_feedbackmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='email',
            field=models.EmailField(
                default=None,
                help_text='This will help use to reach you when we launch a new version of the application',
                max_length=254,
                verbose_name='Email Address',
            ),
        ),
    ]
