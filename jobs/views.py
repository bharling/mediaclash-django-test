from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ExpressionOfInterestForm, ImNotInterestedForm
from newsletters.mixins import NewsletterSignupMixin

# Create your views here.

class ExpressYourInterestView(NewsletterSignupMixin, FormView):
	"""
	Users interested in our company can let us know here
	"""
	template_name = 'express_interest.html'
	form_class = ExpressionOfInterestForm
	success_url = '/thanks/'

	optin_field = 'sign_up_to_newsletter'

	def form_valid(self, form):
		print 'Sending email to the admins'
		return super(ExpressYourInterestView, self).form_valid(form)



class NotInterestedView(NewsletterSignupMixin, FormView):
	"""
	Those absolutely NOT interested can let us know as well
	"""

	template_name = 'not_interested.html'
	form_class = ImNotInterestedForm
	success_url = '/thanks/?but=not_interested'

	optin_field = 'signup_for_spam_emails'
	email_field = 'email_address'

	def get_subscriber_name(self, form):
		return " ".join([
			form.cleaned_data['first_name'], 
			form.cleaned_data['last_name']]
		)

	def form_valid(self, form):
		print "Letting those admins know"
		return super(NotInterestedView, self).form_valid(form)

class ThanksView(TemplateView):
	template_name = 'thanks.html'

	def get_context_data(self, **kwargs):
	    context = super(ThanksView, self).get_context_data(**kwargs)
	    if self.request.GET.get('but', None):
	    	context['fine_then'] = True
	    return context
		
		