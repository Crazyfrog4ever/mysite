# Generated by Django 5.0.3 on 2024-03-28 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_read_private_section', 'VIP User'), ('user_watcher', 'User_watcher'))},
        ),
    ]
