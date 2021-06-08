from django.db import models

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Article(Page):
    # Define body: allow choices/combos from two elements; ordered by editors
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('twitter', EmbedBlock()),
    ], blank=True)

    # Define images associated in the article
    icon_rgb = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Icon RGB',
    )
    icon_reverse = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Icon Reverse'
    )
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Banner Image'
    )

    # define author of the article
    author_info = models.ForeignKey(
        'author.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Author'
    )

    # define properties of Article as that of author_info
    @property
    def author_title(self):
        return self.author_info.title

    @property
    def author_bio(self):
        return self.author_info.bio

    @property
    def author_image(self):
        return self.author_info.main_image

    # define panels appear to the editors
    content_panels = Page.content_panels + [
        FieldPanel('author_info'),
        StreamFieldPanel('body'),
        ImageChooserPanel('icon_rgb'),
        ImageChooserPanel('icon_reverse'),
        ImageChooserPanel('banner_image'),
    ]


