# Generated by Django 5.1.3 on 2024-11-26 09:48

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_comment'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
