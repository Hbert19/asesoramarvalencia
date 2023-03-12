# Generated by Django 2.2.1 on 2023-03-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testimonials', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contacto',
            },
        ),
        migrations.CreateModel(
            name='Gifcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
            ],
            options={
                'verbose_name': 'Gifcard',
                'verbose_name_plural': 'Gifcard',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen 1')),
                ('header_image2', models.FileField(blank=True, upload_to='', verbose_name='Imagen 2')),
                ('header_image3', models.FileField(blank=True, upload_to='', verbose_name='Imagen 3')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
                ('section_1_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_1_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_1_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('section_2_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_2_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_3_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_3_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_4_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_4_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_4_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home',
            },
        ),
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
                ('section_1_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_1_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_1_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('section_2_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_2_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_3_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_3_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_4_parallax', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('section_4_parallax_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Hombres',
                'verbose_name_plural': 'Hombres',
            },
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
                ('section_1_subtitle', models.CharField(blank=True, max_length=100, verbose_name='Subtítulo')),
                ('section_1_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_1_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_2_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_2_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_2_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('section_3_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_3_description', models.TextField(blank=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Mujeres',
                'verbose_name_plural': 'Mujeres',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
                ('section_1_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_1_description', models.TextField(blank=True, verbose_name='Descripción')),
                ('section_2_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_3_parallax', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('section_3_parallax_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('product', models.ManyToManyField(blank=True, to='products.Products')),
            ],
            options={
                'verbose_name': 'Servicios',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Título del Header')),
                ('section_1_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('section_1_subtitle', models.CharField(blank=True, max_length=100, verbose_name='Subtítulo')),
                ('section_1_description', models.TextField(blank=True, verbose_name='Drescripción')),
                ('section_1_image', models.FileField(blank=True, upload_to='', verbose_name='Imagen')),
                ('testimonial_title', models.CharField(blank=True, max_length=100, verbose_name='Título')),
                ('testimonial', models.ManyToManyField(blank=True, to='testimonials.Testimonial', verbose_name='Testimonios')),
            ],
            options={
                'verbose_name': 'Sobre mi',
                'verbose_name_plural': 'Sobre mi',
            },
        ),
    ]