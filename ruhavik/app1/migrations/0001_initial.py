# Generated by Django 4.0.6 on 2022-07-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(blank=True, max_length=100, null=True)),
                ('car_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_chat_id', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_username', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
            ],
        ),
        migrations.CreateModel(
            name='Unique_km',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip_and_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_sheet', models.BooleanField(blank=True, null=True)),
                ('documents_check', models.BooleanField(blank=True, null=True)),
                ('check_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheels_and_running_gear_check_photo1', models.ImageField(blank=True, null=True, upload_to='images/gear')),
                ('wheels_and_running_gear_check_photo2', models.ImageField(blank=True, null=True, upload_to='images/gear')),
                ('oil_check_photo2', models.ImageField(blank=True, null=True, upload_to='images/oil')),
                ('odometer_and_dashboard_readings_data', models.CharField(blank=True, max_length=40, null=True)),
                ('odometer_and_dashboard_readings_data_photo', models.ImageField(blank=True, null=True, upload_to='images/odometer')),
                ('tablet_connection', models.BooleanField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Refueling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liter', models.CharField(blank=True, max_length=30, null=True)),
                ('refueling_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Police_problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Malfunctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunctions_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Lunch_stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_in_zone_photo', models.ImageField(blank=True, null=True, upload_to='images/car')),
                ('alarm_check', models.BooleanField(blank=True, null=True)),
                ('car_checkout', models.BooleanField(blank=True, null=True)),
                ('launc_stop', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='End',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_stop', models.BooleanField(blank=True, null=True)),
                ('odometer_and_dashboard_readings_data', models.CharField(blank=True, max_length=40, null=True)),
                ('odometer_and_dashboard_readings_data_photo', models.ImageField(blank=True, null=True, upload_to='images/odometer')),
                ('camera_stop', models.BooleanField(blank=True, null=True)),
                ('camera_check_photo1', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('camera_check_photo2', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('camera_check_photo3', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('camera_check_photo4', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('construction_check', models.ImageField(blank=True, null=True, upload_to='images/construction')),
                ('alarm_check', models.BooleanField(blank=True, null=True)),
                ('camera_cover', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Dtp_or_chp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtp_or_chp_date', models.DateTimeField(auto_now_add=True)),
                ('dtp_or_chp_photo1', models.ImageField(blank=True, null=True, upload_to='images/dtp')),
                ('dtp_or_chp_photo2', models.ImageField(blank=True, null=True, upload_to='images/dtp')),
                ('dtp_or_chp_photo3', models.ImageField(blank=True, null=True, upload_to='images/dtp')),
                ('dtp_or_chp_photo4', models.ImageField(blank=True, null=True, upload_to='images/dtp')),
                ('dtp_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Dinner_stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_in_zone_photo', models.ImageField(blank=True, null=True, upload_to='images/car')),
                ('alarm_check', models.BooleanField(blank=True, null=True)),
                ('car_checkout', models.BooleanField(blank=True, null=True)),
                ('dinner_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeSSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssd_new', models.CharField(blank=True, max_length=50, null=True)),
                ('ssd_old', models.CharField(blank=True, max_length=50, null=True)),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
        migrations.CreateModel(
            name='CameraCheckin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_check', models.BooleanField(blank=True, null=True)),
                ('support_st_check_photo', models.ImageField(blank=True, null=True, upload_to='images/support')),
                ('chips_and_abrasions_check_photo1', models.ImageField(blank=True, null=True, upload_to='images/chips')),
                ('chips_and_abrasions_check_photo2', models.ImageField(blank=True, null=True, upload_to='images/chips')),
                ('chips_and_abrasions_check_photo3', models.ImageField(blank=True, null=True, upload_to='images/chips')),
                ('chips_and_abrasions_check_photo4', models.ImageField(blank=True, null=True, upload_to='images/chips')),
                ('camera_start_photo', models.ImageField(blank=True, null=True, upload_to='images/camera')),
                ('ssd_date_check', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.car')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
        ),
    ]
