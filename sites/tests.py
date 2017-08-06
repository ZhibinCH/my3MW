from django.test import TestCase
from .models import Sites


class SitesModelTests(TestCase):

    def test_was_table_created(self):
        """
        exists() returns True for an object already exists in database.
        """
        site = Sites(site_name='Demo Site', site_id='1',date='2015-02-01',a_value = '12',b_value='16')
        
         
        self.assertIs(site.site_name=='Demo Site', True)

# Create your tests here.
