from django.test import TestCase
from .models import Contact

# test contact models
class ContactTestCase(TestCase):
    def setUp(self):
        """Create model objects."""
        Contact.objects.create(
            name='Jane Doe',
            email='janedoe@gmail.com',
            phone='+2348123940567',
            subject='Sample Subject',
            message='This is my test message for Contact object.'
        )


    # def test_user_can_compose_message(self):
    #     """ Test whether a user can compose a messsage in the contact form."""
    #     test_user = Contact.objects.get(name='Jane Doe')
    #     self.assertEqual(test_user.email, 'janedoe@gmail.com')
    #     self.assertEqual(test_user.phone, '+2348123940567')
    #     self.assertEqual(test_user.subject, 'Sample Subject')
    #     self.assertEqual(
    #         test_user.message, 
    #         'This is my test message for Contact object.'
    #         )

    def test_user_can_compose_message(self):
        """ Test whether a user can compose a messsage in the contact form."""
        test_user = Contact.objects.get(name='Jane Doe')
        test_cases = {'email': 'janedoe@gmail.com', 'phone': '+2348123940567', 'subject': 'Sample Subject', 'message': 'This is my test message for Contact object.'}
        for field, value in test_cases.items():
            with self.subTest("wrong user subtest", field=field, ):
                self.assertEqual(getattr(test_user, field), value)

    
    def test_string_representation(self):
        """ 
        Tests that a human readable representation of the object is returned.
        """
        contact = Contact(message='A string representation of the model\'s object.')
        self.assertEqual(str(contact), contact.message)


# test contact views
