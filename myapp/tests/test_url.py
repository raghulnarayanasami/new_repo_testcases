from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import user_login, s3bucket, storagedata



class TestUrls(SimpleTestCase):

    def test_login_url_resloves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, user_loginss)

    def test_s3bucket_url_resolves(self):
        url = reverse('s3bucket')
        self.assertEquals(resolve(url).func, s3bucket)

    def test_storage_url_resloves(self):
        url = reverse('storage')
        self.assertEquals(resolve(url).func, storagedata)
