from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
# from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Author(Page):
    bio = models.CharField(blank=True, max_length=255)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('bio'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(Author, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]