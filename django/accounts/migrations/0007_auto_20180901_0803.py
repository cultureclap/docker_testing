# Generated by Django 2.0.1 on 2018-09-01 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180901_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userjurisdictions',
            name='admin_level',
        ),
        migrations.AddField(
            model_name='userjurisdictions',
            name='info_level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'complete'), (1, 'basic'), (2, 'minimal')], default=0),
        ),
        migrations.AlterField(
            model_name='activistorgs',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Organization'),
        ),
    ]