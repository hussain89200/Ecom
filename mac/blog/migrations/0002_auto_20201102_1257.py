# Generated by Django 3.1.2 on 2020-11-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
