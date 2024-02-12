# Generated by Django 5.0.1 on 2024-01-11 17:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelled_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('Workshop_Name', models.CharField(max_length=100, null=True)),
                ('Cancel_reason', models.TextField(max_length=100, null=True)),
                ('Area', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receive_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Workshop_Name', models.CharField(max_length=100, null=True)),
                ('Service_Type', models.TextField(max_length=100, null=True)),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('Vehicle_Brand', models.CharField(max_length=100, null=True)),
                ('Vehicle_Registration_Number', models.CharField(max_length=100, null=True)),
                ('Completion_Date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Completion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Workshop_Name', models.CharField(max_length=100, null=True)),
                ('Service_Type', models.TextField(max_length=100, null=True)),
                ('Vehicle_Brand', models.CharField(max_length=100, null=True)),
                ('Delivery_Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Bill_amount', models.CharField(max_length=100, null=True)),
                ('Invoice', models.FileField(null=True, upload_to='media/Invoice')),
                ('Vehicle_Registration_No', models.CharField(max_length=100, null=True)),
                ('Rating', models.IntegerField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Workshop_Name', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('trade_license', models.FileField(null=True, upload_to='media/trade_license')),
                ('certifications', models.FileField(null=True, upload_to='media/certifications')),
                ('Owner_Voter_ID', models.FileField(null=True, upload_to='media/Owner_Voter_ID')),
                ('Contact_Number', models.CharField(max_length=100, null=True)),
                ('Password', models.CharField(max_length=100, null=True)),
                ('confirm_Password', models.CharField(max_length=100, null=True)),
                ('Number_of_employee', models.CharField(max_length=100, null=True)),
                ('owner_photo', models.ImageField(null=True, upload_to='media/owner_photo')),
                ('Workshop_Photo', models.ImageField(null=True, upload_to='media/Workshop_Photo')),
                ('TIN', models.CharField(max_length=100, null=True)),
                ('Service_Type', models.TextField(max_length=100, null=True)),
                ('Vehicle_Brand', models.CharField(max_length=100, null=True)),
                ('Rating', models.IntegerField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Profile_Photo', models.ImageField(null=True, upload_to='media/Profile_Photo')),
                ('display_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('voter_id_no', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]