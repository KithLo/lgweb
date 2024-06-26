# Generated by Django 4.1.5 on 2023-04-08 14:29

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=45, verbose_name='IP')),
                ('fingerprint', models.CharField(max_length=64)),
                ('language', models.TextField(choices=[('tc', '繁體'), ('sc', '简体')])),
                ('url', models.TextField()),
                ('user_agent', models.TextField()),
                ('referrer', models.TextField()),
            ],
            options={
                'db_table': 'analytics',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='banner/image/')),
                ('font', models.FileField(blank=True, upload_to='banner/font/')),
                ('subfont', models.FileField(blank=True, upload_to='banner/subfont/')),
                ('font_size', models.IntegerField(default=28)),
                ('letter_spacing', models.IntegerField(default=30)),
                ('font_weight', models.IntegerField(choices=[(400, 'Normal'), (700, 'Bold')], default=700)),
                ('font_color', models.CharField(default='#ffffff', max_length=7)),
                ('shadow_x', models.IntegerField(default=10)),
                ('shadow_y', models.IntegerField(default=10)),
                ('shadow_blur', models.IntegerField(default=20)),
                ('shadow_color', models.CharField(default='#000000', max_length=7)),
                ('offset_x', models.IntegerField(default=0)),
                ('offset_y', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=45, verbose_name='IP')),
                ('fingerprint', models.CharField(max_length=64)),
                ('language', models.TextField(choices=[('tc', '繁體'), ('sc', '简体')])),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('language', models.TextField(choices=[('tc', '繁體'), ('sc', '简体')], primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'home_page',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField()),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('title_tc', models.TextField(verbose_name='Title')),
                ('title_sc', models.TextField(verbose_name='Title')),
            ],
            options={
                'db_table': 'menu_item',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('type', models.TextField(choices=[('message', 'Message'), ('topic', 'Topic')], verbose_name='Type')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('publish', models.DateField(blank=True, null=True, verbose_name='Publish at')),
                ('title_tc', models.TextField(blank=True, verbose_name='Title')),
                ('title_sc', models.TextField(blank=True, verbose_name='Title')),
                ('author_tc', models.TextField(blank=True, verbose_name='Author')),
                ('author_sc', models.TextField(blank=True, verbose_name='Author')),
                ('banner_sc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_sc_set', to='app.banner', verbose_name='Banner')),
                ('banner_tc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_tc_set', to='app.banner', verbose_name='Banner')),
            ],
            options={
                'db_table': 'page',
            },
        ),
        migrations.CreateModel(
            name='ParentMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.menuitem')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'db_table': 'parent_menu_item',
                'ordering': ['position'],
            },
            bases=('app.menuitem',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.page')),
                ('is_blog', models.BooleanField(verbose_name='Blog layout')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('end_msg_tc', models.TextField(blank=True, verbose_name='"End" message')),
                ('end_msg_sc', models.TextField(blank=True, verbose_name='"End" message')),
                ('description_tc', models.TextField(blank=True, verbose_name='Description')),
                ('description_sc', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'topic',
            },
            bases=('app.page',),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(upload_to='promotion/image/', verbose_name='Image')),
                ('alt', models.TextField(blank=True, verbose_name='Image Hint')),
                ('title', models.TextField(verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.homepage')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.page')),
            ],
            options={
                'db_table': 'promotion',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.page'),
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField()),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.banner')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.homepage')),
                ('target_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.page')),
            ],
            options={
                'db_table': 'home_banner',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.page')),
                ('position', models.PositiveSmallIntegerField()),
                ('prefix_tc', models.TextField(blank=True, verbose_name='Prefix')),
                ('prefix_sc', models.TextField(blank=True, verbose_name='Prefix')),
                ('document_tc', models.FileField(blank=True, upload_to='message/document/', verbose_name='Document')),
                ('document_sc', models.FileField(blank=True, upload_to='message/document/', verbose_name='Document')),
                ('audio_tc', models.FileField(blank=True, upload_to='message/audio/', verbose_name='Audio')),
                ('audio_sc', models.FileField(blank=True, upload_to='message/audio/', verbose_name='Audio')),
                ('preview_tc', models.TextField(blank=True, verbose_name='Preview')),
                ('preview_sc', models.TextField(blank=True, verbose_name='Preview')),
                ('content_tc', models.TextField(blank=True, verbose_name='Content')),
                ('content_sc', models.TextField(blank=True, verbose_name='Content')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.topic')),
            ],
            options={
                'db_table': 'message',
                'ordering': ['parent', 'position'],
            },
            bases=('app.page',),
        ),
        migrations.CreateModel(
            name='ChildMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.menuitem')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.parentmenuitem')),
            ],
            options={
                'verbose_name': 'Submenu Item',
                'db_table': 'child_menu_item',
                'ordering': ['position'],
            },
            bases=('app.menuitem',),
        ),
    ]
