# Generated by Django 4.1.2 on 2022-11-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_blogs_blogcontent_alter_blogs_blogtopic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomments',
            old_name='blogcontent',
            new_name='commentcontent',
        ),
    ]
