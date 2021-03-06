# Generated by Django 2.2.10 on 2020-08-03 13:09
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oneid_meta.models.config
import uuid


def init_github_config(apps, schema_editor):

    GithubConfig = apps.get_model('oneid_meta', 'GithubConfig')
    Site = apps.get_model('sites', 'Site')

    site, _ = Site.objects.get_or_create(id=settings.SITE_ID)
    GithubConfig.objects.get_or_create(site=site)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('oneid_meta', '0078_i18nmobileconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountconfig',
            name='allow_github',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否开放github账号登录'),
        ),
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('github_user_id', models.CharField(blank=True, max_length=255, verbose_name='Github ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='github_user', to='oneid_meta.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='GithubConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('client_id', models.CharField(blank=True, default='', max_length=255, verbose_name='Client ID')),
                ('client_secret', models.CharField(blank=True, default='', max_length=255, verbose_name='Client Secret')),
                ('client_valid', models.BooleanField(default=False, verbose_name='Client 配置是否正确')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='github_config', to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, oneid_meta.models.config.SingletonConfigMixin),
        ),
        migrations.AddIndex(
            model_name='githubuser',
            index=models.Index(fields=['github_user_id'], name='githubuserid_index'),
        ),
        migrations.RunPython(init_github_config)
    ]
