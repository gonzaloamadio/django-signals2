# Generated by Django 2.0 on 2018-10-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('related', '0001_initial'),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related.Job', verbose_name='Job')),
                ('tester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Person', verbose_name='Person')),
            ],
        ),
    ]
