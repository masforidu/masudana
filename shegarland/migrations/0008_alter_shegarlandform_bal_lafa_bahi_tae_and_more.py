# Generated by Django 5.1.1 on 2024-12-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shegarland', '0007_alter_shegarlandform_bal_lafa_bahi_tae_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shegarlandform',
            name='bal_lafa_bahi_tae',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='bal_lafa_hafe',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='balina_lafa',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=6),
        ),
    ]