# Generated by Django 4.1.2 on 2022-10-30 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_coment_comment_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='liketocomment',
            unique_together={('comment', 'writer')},
        ),
    ]
