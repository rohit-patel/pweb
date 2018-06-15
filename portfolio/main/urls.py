from django.conf.urls import url

from main.views import (HomepageView, MeetAIView, ResumeView, ResearchView,
                        LatexBeamerThemeView, LatexBeamerKelloggView, LatexBeamerNorthWesternView)

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^meet-ai/$', MeetAIView.as_view(), name='meet_ai'),
    url(r'^resume/$', ResumeView.as_view(), name='resume'),
    url(r'^research/$', ResearchView.as_view(), name='research'),
    url(r'^latex-beamer-theme/$', LatexBeamerThemeView.as_view(), name='latex_beamer_theme'),
    url(r'^latex-beamer-presentation-kellogg/$', LatexBeamerKelloggView.as_view(), name='latex_beamer_kellogg'),
    url(r'^latex-beamer-presentation-northwestern/$', LatexBeamerNorthWesternView.as_view(), name='latex_beamer_northwestern'),
]
