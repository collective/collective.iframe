# -*- coding: utf-8 -*-
from collective.iframe.content.iframe import IIframe  # NOQA E501
from collective.iframe.testing import COLLECTIVE_IFRAME_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class IframeIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_IFRAME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_iframe_schema(self):
        fti = queryUtility(IDexterityFTI, name="Iframe")
        schema = fti.lookupSchema()
        self.assertEqual(IIframe, schema)

    def test_ct_iframe_fti(self):
        fti = queryUtility(IDexterityFTI, name="Iframe")
        self.assertTrue(fti)

    def test_ct_iframe_factory(self):
        fti = queryUtility(IDexterityFTI, name="Iframe")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IIframe.providedBy(obj),
            "IIframe not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_iframe_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Iframe",
            id="iframe",
        )

        self.assertTrue(
            IIframe.providedBy(obj),
            "IIframe not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("iframe", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("iframe", parent.objectIds())

    def test_ct_iframe_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Iframe")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))
