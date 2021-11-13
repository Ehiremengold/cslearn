# Generated by Django 3.0.2 on 2021-07-03 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='Duration of the quiz in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='pass score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
