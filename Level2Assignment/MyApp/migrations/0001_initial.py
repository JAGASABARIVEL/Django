# Generated by Django 2.1.1 on 2019-12-07 04:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateTimeField(default=datetime.datetime.now)),
                ('startdate', models.DateField()),
                ('starttime', models.TimeField()),
                ('enddate', models.DateField(blank=True, null=True)),
                ('endtime', models.TimeField(blank=True, null=True)),
                ('startkm', models.IntegerField(default=0)),
                ('endkm', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(default='NEW', max_length=263)),
                ('estimated_amount', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('dieselcost', models.IntegerField(blank=True, null=True)),
                ('tollcost', models.IntegerField(blank=True, null=True)),
                ('policecost', models.IntegerField(blank=True, null=True)),
                ('othercost', models.IntegerField(blank=True, null=True)),
                ('bookinguser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL)),
                ('cancelledby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadtype', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterClient',
            fields=[
                ('name', models.CharField(max_length=260, primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=260)),
                ('referedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterDriver',
            fields=[
                ('name', models.CharField(max_length=260, primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=260)),
                ('referedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterLorry',
            fields=[
                ('lorry_number', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('year_model', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SearchLorry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_to_be_looked', models.DateField()),
                ('loading_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_from', to='MyApp.Places')),
                ('unloading_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_to', to='MyApp.Places')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=260)),
                ('last_name', models.CharField(blank=True, max_length=260)),
                ('password', models.CharField(blank=True, max_length=260)),
                ('confirm_password', models.CharField(blank=True, max_length=260)),
                ('phone', models.IntegerField(blank=True)),
                ('confirm_phone', models.IntegerField(blank=True)),
                ('user_type', models.CharField(choices=[('LO', 'LORRYOWNER'), ('DA', 'DRIVER'), ('AO', 'APPLICATION_OWNER'), ('MA', 'MANAGER'), ('NU', 'NORMALUSER')], default='NU', max_length=2)),
                ('user_blog', models.URLField(blank=True)),
                ('user_image', models.ImageField(blank=True, upload_to='user_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicletype', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='registerlorry',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.VehicleType'),
        ),
        migrations.AddField(
            model_name='booking',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.RegisterClient'),
        ),
        migrations.AddField(
            model_name='booking',
            name='completedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='driverid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.RegisterDriver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='from_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_from_place', to='MyApp.Places'),
        ),
        migrations.AddField(
            model_name='booking',
            name='load_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.LoadType'),
        ),
        migrations.AddField(
            model_name='booking',
            name='lorryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.RegisterLorry'),
        ),
        migrations.AddField(
            model_name='booking',
            name='staginguser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staging_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='to_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_to_place', to='MyApp.Places'),
        ),
    ]
