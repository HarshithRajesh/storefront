# Generated by Django 4.2.2 on 2023-07-01 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection')
        """ ,"""
            DELETE FROM store_colletion
            WHERE title = 'collecton'
        """)
    ]
