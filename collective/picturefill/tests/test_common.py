import unittest2 as unittest
from collective.picturefill.tests import base
from collective.picturefill import common
from collective.picturefill.common import PictureFill


class UnitTestCommon(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_getPictures(self):
        base_url = 'http://nohost/plone/myimage/@@images/image/'
        pictures, noscript = common.getPictures(base_url, self.sizes)
        self.assertEqual(len(pictures), 4)
        thumb_url = base_url + 'thumb'
        self.assertEqual(noscript, thumb_url)
        for picture in pictures[:-1]:
            self.assertTrue(picture['src'].startswith(base_url))
            self.assertTrue(picture['media'].startswith('(max-width: '))
            self.assertTrue(picture['media'].endswith('px)'))
            width = picture['media'][12:-3]
            self.assertTrue(width.isdigit())
        #test the last
        picture = pictures[-1]
        self.assertTrue(picture['src'].startswith(base_url[:-1]))
        self.assertTrue(picture['media'].startswith('(min-width: '))
        self.assertTrue(picture['media'].endswith('px)'))
        width = picture['media'][12:-3]
        self.assertTrue(width.isdigit())

    def test_picturefill_view(self):
        view = PictureFill(self.context, self.request)
        view.sizes = self.sizes
        view.update()


class IntegrationTestCommon(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_getPictures(self):
        base_url = 'http://nohost/plone/myimage/@@images/image/'
        from plone.app.imaging.utils import getAllowedSizes
        sizes = getAllowedSizes()
        pictures, noscript = common.getPictures(base_url, sizes)
        self.assertEqual(len(pictures), 8)
        thumb_url = base_url + 'thumb'
        self.assertEqual(noscript, thumb_url)
        for picture in pictures[:-1]:
            self.assertTrue(picture['src'].startswith(base_url))
            self.assertTrue(picture['media'].startswith('(max-width: '))
            self.assertTrue(picture['media'].endswith('px)'))
            width = picture['media'][12:-3]
            self.assertTrue(width.isdigit())
        #test the last
        picture = pictures[-1]
        self.assertTrue(picture['src'].startswith(base_url[:-1]))
        self.assertTrue(picture['media'].startswith('(min-width: '))
        self.assertTrue(picture['media'].endswith('px)'))
        width = picture['media'][12:-3]
        self.assertTrue(width.isdigit())


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)