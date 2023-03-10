# Generated by Django 4.1.1 on 2022-10-17 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_studentaccount'),
        ('manager', '0006_delete_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=1)),
                ('timefrom', models.TimeField()),
                ('timeto', models.TimeField()),
                ('s_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.class')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.school')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.teacheraccount')),
            ],
        ),
    ]
