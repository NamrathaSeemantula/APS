# Generated by Django 4.1.2 on 2022-11-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postcomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='postcomments',
            new_name='postscomments',
        ),
    ]
