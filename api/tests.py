from django.test import TestCase
from .models import PuppyOwner
from rest_framework import status
from django.urls import reverse
# Create your tests here.


class ModelTestCase(TestCase):
    """This Class Defines the test suite for the PuppyOwner model"""

    def setUp(self):
        """define the test client and other test variables"""
        self.puppyOwner_name = "Owner1"
        self.puppyOwner_email = "email@test.com"
        self.puppyOwner = PuppyOwner(name=self.puppyOwner_name, email=self.puppyOwner_email)
        print ('test1 completed')



    def test_model_can_create_a_petOwner(self):
        """Tests if a new PuppyOwner Object can be created"""
        old_count = PuppyOwner.objects.count()
        self.puppyOwner.save()
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

