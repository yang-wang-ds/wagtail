# Generated by Django 3.2.4 on 2021-06-07 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('article', '0002_auto_20210607_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iconone',
            name='image',
        ),
        migrations.RemoveField(
            model_name='iconone',
            name='page',
        ),
        migrations.RemoveField(
            model_name='icontwo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='icontwo',
            name='page',
        ),
        migrations.AddField(
            model_name='article',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='icon_reverse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Icon Reverse'),
        ),
        migrations.AddField(
            model_name='article',
            name='icon_rgb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Icon RGB'),
        ),
        migrations.DeleteModel(
            name='BackgroundImage',
        ),
        migrations.DeleteModel(
            name='IconOne',
        ),
        migrations.DeleteModel(
            name='IconTwo',
        ),
    ]
