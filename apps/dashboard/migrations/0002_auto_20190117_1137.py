# Generated by Django 2.1.5 on 2019-01-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklog',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'TODO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('DONE', 'DONE')], default='TODO', max_length=255),
        ),
    ]
