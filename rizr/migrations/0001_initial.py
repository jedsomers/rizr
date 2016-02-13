# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=20)),
                ('datetime', models.CharField(max_length=265)),
                ('ageHrs', models.DecimalField(max_digits=12, decimal_places=4)),
                ('commentCount', models.IntegerField(default=0)),
                ('likeCount', models.IntegerField(default=0)),
                ('dislikeCount', models.IntegerField(default=0)),
                ('favoriteCount', models.IntegerField(default=0)),
                ('expviews', models.DecimalField(max_digits=12, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20)),
                ('buyDate', models.CharField(max_length=265)),
                ('buyPx', models.DecimalField(max_digits=12, decimal_places=4)),
                ('currentDate', models.CharField(max_length=265)),
                ('currentPx', models.DecimalField(max_digits=12, decimal_places=4)),
                ('amount', models.IntegerField(default=0)),
                ('earnedPerc', models.DecimalField(max_digits=10, decimal_places=4)),
                ('earnedTot', models.DecimalField(max_digits=12, decimal_places=4)),
                ('timeHeldHrs', models.DecimalField(max_digits=12, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Txhistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20)),
                ('buyDate', models.CharField(max_length=265)),
                ('buyPx', models.DecimalField(max_digits=12, decimal_places=4)),
                ('sellDate', models.CharField(max_length=265)),
                ('sellPx', models.DecimalField(max_digits=12, decimal_places=4)),
                ('amount', models.IntegerField(default=0)),
                ('earnedPerc', models.DecimalField(max_digits=10, decimal_places=4)),
                ('earnedTot', models.DecimalField(max_digits=12, decimal_places=4)),
                ('timeHeldHrs', models.DecimalField(max_digits=12, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('networth', models.DecimalField(max_digits=12, decimal_places=4)),
                ('trades', models.IntegerField(default=0)),
                ('admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=20)),
                ('date_up', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='txhistory',
            name='user',
            field=models.ForeignKey(to='rizr.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='txhistory',
            name='video',
            field=models.ForeignKey(to='rizr.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(to='rizr.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='video',
            field=models.ForeignKey(to='rizr.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='video',
            field=models.ForeignKey(to='rizr.Video'),
            preserve_default=True,
        ),
    ]
