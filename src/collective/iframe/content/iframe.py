from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item

# from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from collective.iframe import _


class IIframe(model.Schema):
    """Marker interface and Dexterity Python Schema for Iframe

    For inspiration for more fields:
    https://github.com/collective/Products.windowZ/blob/master/Products/windowZ/content/Window.py
    https://github.com/collective/collective.tiles.iframembed/blob/master/src/collective/tiles/iframembed/interfaces.py

    Products.windowZ has:
    hide_metadata
    use_base_url
    catalog_page_content
    show_reference
    inherit_protocol
    """

    remote_url = schema.URI(
        title=_("label_url_to_embed", "Url to embed"), required=False
    )

    page_width = schema.TextLine(
        title=_("Page width"),
        # TODO: text taken over from Products.windowZ
        # Not sure if we want to have a control panel.
        description=_(
            "help_page_width",
            default=(
                "Enter a value for the page width. If it is not provided, "
                "the page width will assume the default value defined in "
                "the site setup. You may use %, px, em, etc."
            ),
        ),
        required=False,
    )

    page_height = schema.TextLine(
        title=_("Page height"),
        description=_(
            "help_page_height",
            default=(
                "Enter a value for the page height. If it is not provided, "
                "the page height will assume the default value defined in "
                "the site setup. You may use %, px, em, etc."
            ),
        ),
        required=False,
    )

    text_above = RichText(title=_("Text above"), required=False)

    text_below = RichText(title=_("Text below"), required=False)


@implementer(IIframe)
class Iframe(Item):
    """Content-type class for IIframe"""
