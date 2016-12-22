from .utils import signup_newsletter

class NewsletterSignupMixin(object):

	email_field = 'email'
	name_field = 'name'
	optin_field = 'optin_comms'

	def get_subscriber_email(self, form):
		return form.cleaned_data[self.email_field]

	def get_subscriber_name(self, form):
		return form.cleaned_data[self.name_field]

	def form_valid(self, form):
		if form.cleaned_data.get(self.optin_field) == True:
			name = self.get_subscriber_name(form)
			email = self.get_subscriber_email(form)
			signup_newsletter(email, name)
