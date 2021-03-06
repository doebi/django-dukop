# Generated by Django 2.1.14 on 2019-11-28 23:38
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='group',
            name='is_restricted',
            field=models.BooleanField(default=False, help_text='Do not allow others to add events to this group'),
        ),
        migrations.AddField(
            model_name='user',
            name='token_expiry',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token_passphrase',
            field=models.CharField(help_text='One time passphrase', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
