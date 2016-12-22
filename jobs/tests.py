from django.test import TestCase
import mock
from django.test import RequestFactory
from .views import ExpressYourInterestView, NotInterestedView

# Create your tests here.

class FormTests(TestCase):

	def test_interest_signup_newsletter(self):
		request = RequestFactory().post(
			'/interested/', #
			data={
				"email":"test@example.com",
				"name":"Test User",
				"what_interests_you":"Not Much",
				"sign_up_to_newsletter":True
			}
		)

		view = ExpressYourInterestView.as_view()

		with mock.patch('newsletters.mixins.signup_newsletter') as mock_signup:
			response = view(request)
			mock_signup.assert_called_with('test@example.com', 'Test User')

	def test_not_interested_signs_up_to_spam(self):
		request = RequestFactory().post(
			'/not-interested/', #
			data={
				"email_address":"test@example.com",
				"first_name":"Test",
				"last_name":"User",
				"reason_for_no_interest":"Not Much",
				"telephone_number":"None of your beeswax",
				"postal_address":"See above",
				"signup_for_spam_emails":True
			}
		)

		view = NotInterestedView.as_view()
		with mock.patch('newsletters.mixins.signup_newsletter') as mock_signup:
			response = view(request)
			mock_signup.assert_called_with('test@example.com', 'Test User')


