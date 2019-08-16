# Generated by Django 2.2.3 on 2019-08-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_auto_20190806_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='formation image base64 data'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='name',
            field=models.CharField(default='custom', max_length=30, verbose_name='Name of formation'),
        ),
    ]