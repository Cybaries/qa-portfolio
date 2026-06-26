# Generated migration — works with both SQLite and MongoDB.
# When MONGO_URI is set, DEFAULT_AUTO_FIELD in settings.py is
# ObjectIdAutoField, so Django creates collections with ObjectId PKs.
# When MONGO_URI is not set, DEFAULT_AUTO_FIELD is BigAutoField (SQLite).
# A single migration file handles both; no AlterField step needed.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(default='Present', max_length=50)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('tech_stack', models.CharField(max_length=300)),
                ('date_range', models.CharField(blank=True, max_length=100)),
                ('severity', models.CharField(
                    choices=[('critical', 'Critical'), ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
                    default='high', max_length=20)),
                ('github_url', models.URLField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stage', models.CharField(
                    choices=[('plan', 'Plan'), ('code', 'Code'), ('build', 'Build'),
                             ('test', 'Test'), ('release', 'Release'), ('monitor', 'Monitor')],
                    max_length=20)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['stage', 'order']},
        ),
        migrations.CreateModel(
            name='ExperienceBullet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('experience', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='bullets', to='core.experience')),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='ProjectBullet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('project', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='bullets', to='core.project')),
            ],
            options={'ordering': ['order']},
        ),
    ]
