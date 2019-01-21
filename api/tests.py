from django.test import TestCase
from .models import PuppyOwner
from rest_framework import status
from django.urls import reverse
# Create your tests here.

# Thing here to note: We don't use the default django test framework (which is based on unittest),
# we use the more advanced pytest.  So my comments here will be more general, because they won't
# map as directly to real tests you write

class ModelTestCase(TestCase):
    """This Class Defines the test suite for the PuppyOwner model"""

    def setUp(self):
        """define the test client and other test variables"""
        # If puppyOwner is being assigned to a self attribute, there's no real value in also
        # assigning the name and email to self attributes.  We want to avoid polluting namespaces
        # with unneeded data, because it's an extra place to keep that data updated, and it can
        # be misleading to other developers
        self.puppyOwner_name = "Owner1"
        self.puppyOwner_email = "email@test.com"
        self.puppyOwner = PuppyOwner(name=self.puppyOwner_name, email=self.puppyOwner_email)
        # 2 things here:
        # 1) You don't need to report that a test is completed in the test - the framework will take care of that
        # 2) This isn't a test, it's setup ;)
        print ('test1 completed')


    def test_model_can_create_a_petOwner(self):
        """Tests if a new PuppyOwner Object can be created"""
        # For test methods, we usually add docstrings of the format:
        # Should <expected behaviour>
        # e.g.
        # Should increase total object count when a newe record is created
        old_count = PuppyOwner.objects.count()
        self.puppyOwner.save()
        # generally speaking, it's not valuable to test framework functionality - we only test our
        # own code.  This test is just calling methods inherited from the Django ORM classes.
        # Still, it's always safer to add more tests than fewer, so when in doubt, test it.
        new_count = PuppyOwner.objects.count()
        self.assertNotEqual(old_count, new_count)
        print('test2 completed')

class ViewTestCase(TestCase):

    def test_api_can_create_a_bucketlist(self):
        puppyOwner_data = {'name': 'Owner1', 'email': 'test@test.com'}
        response = self.client.post(
            reverse('create'),
            puppyOwner_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
