from django.contrib.auth.models import User
from django.test import TestCase, modify_settings, override_settings


class TestDataMixin(object):

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(username='super', password='secret', email='super@example.com')


@override_settings(ROOT_URLCONF='admin_docs.urls')
@modify_settings(INSTALLED_APPS={'append': 'django.contrib.admindocs'})
class AdminDocsTestCase(TestCase):
    pass
