# Generated by Django 5.1.6 on 2025-03-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievement_images/')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='Order on the homepage/achievements section.')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['display_order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cause_images/')),
                ('goal_description', models.CharField(blank=True, help_text="Optional: e.g., 'Fundraising Target: $5,000'", max_length=100)),
                ('donation_link', models.URLField(blank=True, help_text='Link to specific donation page for this cause, if any.')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='Order on the causes page.')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['display_order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='team_images/')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='Order on the about page.')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['display_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon_class', models.CharField(blank=True, help_text="e.g., 'fa fa-handshake-o'. Requires Font Awesome.", max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0, help_text='Order on the about page.')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['display_order', 'name'],
            },
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['display_order', 'name']},
        ),
        migrations.RenameField(
            model_name='program',
            old_name='description',
            new_name='full_description',
        ),
        migrations.AddField(
            model_name='program',
            name='display_order',
            field=models.PositiveIntegerField(default=0, help_text='Order on the programs page (lower numbers first).'),
        ),
        migrations.AddField(
            model_name='program',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='program',
            name='short_description',
            field=models.CharField(blank=True, help_text='Brief description for summaries.', max_length=250),
        ),
        migrations.AlterField(
            model_name='program',
            name='key_activities',
            field=models.TextField(blank=True, help_text='List key activities, perhaps one per line.'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
