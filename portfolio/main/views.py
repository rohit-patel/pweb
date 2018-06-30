# Create your views here.
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from .models import Skill, AIProject, Research
from .forms import ContactForm

class HomepageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['skills'] = Skill.objects.all()
		return context


class MeetAIView(TemplateView):
	template_name = 'meet_ai.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ai_projects'] = AIProject.objects.all()
		return context


class ResumeView(CreateView):
	template_name = 'resume.html'
	form_class = ContactForm

	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		self.object = form.save()
		messages.success(self.request, "Thanks for submitting contact us form, I'll get back to you")
		return super().form_valid(form)

	def get_success_url(self):
		return self.request.path


class ResearchView(TemplateView):
	template_name = 'research.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['researches'] = Research.objects.all()
		return context


class LatexBeamerThemeView(TemplateView):
	template_name = 'latex_beamer.html'


class LatexBeamerKelloggView(TemplateView):
	template_name = 'latex_beamer_kellogg.html'


class LatexBeamerNorthWesternView(TemplateView):
	template_name = 'latex_beamer_northwestern.html'


class DetectionView(TemplateView):
	template_name = 'detection.html'

	def post(self, request, *args, **kwargs):
		def post(self, request, *args, **kwargs):
			image = request.FILES.get('image')
			return JsonResponse({'image':'',},status=200)
