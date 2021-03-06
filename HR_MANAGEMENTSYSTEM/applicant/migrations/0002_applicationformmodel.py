# Generated by Django 2.2.9 on 2020-02-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationformModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('qualification', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=30)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('resume', models.FileField(upload_to='Application_Resumes/')),
            ],
        ),
    ]
