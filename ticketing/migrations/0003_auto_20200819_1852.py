# Generated by Django 3.1 on 2020-08-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_cinema'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinema',
            options={'verbose_name': 'سينما', 'verbose_name_plural': 'سينما'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'فيلم', 'verbose_name_plural': 'فيلم'},
        ),
        migrations.AlterField(
            model_name='cinema',
            name='address',
            field=models.TextField(verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='capacity',
            field=models.IntegerField(verbose_name='ظرفيت'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(default='تهران', max_length=30, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام سينما'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='توضيحات'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, verbose_name='كارگردان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.IntegerField(verbose_name='مدت زمان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(verbose_name='سال توليد'),
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='زمان شروع نمايش')),
                ('price', models.IntegerField(verbose_name='قيمت')),
                ('salable_seats', models.IntegerField(verbose_name='صندل هاي قابل فروش')),
                ('free_seats', models.IntegerField(verbose_name='صندلي خالي')),
                ('status', models.IntegerField(choices=[(1, 'فروش شروع نشده'), (2, 'در حال فروش بليط'), (3, 'بليط تمام شد'), (4, 'فروش بليط بسته شد'), (5, 'فيلم پخش شد'), (6, 'سانس لغو شد')], verbose_name='وضعيت')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.cinema', verbose_name='سينما')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.movie', verbose_name='فيلم')),
            ],
            options={
                'verbose_name': 'سانس',
                'verbose_name_plural': 'سانس',
            },
        ),
    ]