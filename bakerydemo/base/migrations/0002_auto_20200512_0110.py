# Generated by Django 3.0.6 on 2020-05-12 01:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('blog', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='people',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_1',
            field=models.ForeignKey(blank=True, help_text='First featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Featured section 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_2',
            field=models.ForeignKey(blank=True, help_text='Second featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Featured section 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_3',
            field=models.ForeignKey(blank=True, help_text='Third featured section for the homepage. Will display up to six child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Featured section 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero CTA link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promo_image',
            field=models.ForeignKey(blank=True, help_text='Promo image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='gallerypage',
            name='collection',
            field=models.ForeignKey(blank=True, help_text='Select the image collection for this gallery.', limit_choices_to=models.Q(_negated=True, name__in=['Root']), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Collection'),
        ),
        migrations.AddField(
            model_name='gallerypage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='formpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.CustomImage'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='base.FormPage'),
        ),
    ]
