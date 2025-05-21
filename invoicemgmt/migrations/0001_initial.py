from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('po_box', models.CharField(max_length=50, blank=True, null=True)),
                ('city', models.CharField(max_length=100, blank=True, null=True)),
                ('country', models.CharField(max_length=100, blank=True, null=True)),
                ('phone', models.CharField(max_length=50, blank=True, null=True)),
                ('fax', models.CharField(max_length=50, blank=True, null=True)),
                ('vat_number', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(unique=True)),
                ('invoice_date', models.DateField()),
                ('vat_number', models.CharField(max_length=100)),
                ('po_number', models.CharField(max_length=100, blank=True, null=True)),
                ('po_date', models.DateField(blank=True, null=True)),
                ('delivery_note', models.CharField(max_length=100, blank=True, null=True)),
                ('do_date', models.DateField(blank=True, null=True)),
                ('ship_to', models.CharField(max_length=255, blank=True, null=True)),
                ('total_taxable', models.DecimalField(max_digits=10, decimal_places=2, default=0)),
                ('total_vat', models.DecimalField(max_digits=10, decimal_places=2, default=0)),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2, default=0)),
                ('amount_in_words', models.CharField(max_length=512, blank=True)),
                ('payment_method', models.CharField(max_length=100, blank=True, null=True, default='CDC')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicemgmt.customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('vat_rate', models.DecimalField(max_digits=4, decimal_places=2, default=5.00)),
                ('vat_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('invoice', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='line_items',
                           to='invoicemgmt.invoice'
                )),
            ],
        ),
    ]
    