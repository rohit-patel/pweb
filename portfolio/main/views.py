from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'home.html'


class MeetAIView(TemplateView):
    template_name = 'meet_ai.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


class ResearchView(TemplateView):
    template_name = 'research.html'


class LatexBeamerThemeView(TemplateView):
    template_name = 'latex_beamer.html'


class LatexBeamerKelloggView(TemplateView):
    template_name = 'latex_beamer_kellogg.html'


class LatexBeamerNorthWesternView(TemplateView):
    template_name = 'latex_beamer_northwestern.html'
