from django.shortcuts import render
from .models import Experience, Project, Skill

STAGE_ORDER = ['plan', 'code', 'build', 'test', 'release', 'monitor']
STAGE_ICONS = {
    'plan': '📋', 'code': '💻', 'build': '🔨',
    'test': '🧪', 'release': '🚀', 'monitor': '📊',
}

def home(request):
    skills = Skill.objects.all()

    # Build ordered list of (stage, icon, [skill_names]) for template
    skills_by_stage_raw = {}
    for s in skills:
        skills_by_stage_raw.setdefault(s.stage, []).append(s.name)

    pipeline_stages = [
        {'key': stage, 'icon': STAGE_ICONS.get(stage, ''), 'skills': skills_by_stage_raw.get(stage, [])}
        for stage in STAGE_ORDER
        if stage in skills_by_stage_raw
    ]

    context = {
        'experiences': Experience.objects.prefetch_related('bullets').all(),
        'projects': Project.objects.prefetch_related('bullets').all(),
        'pipeline_stages': pipeline_stages,
    }
    return render(request, 'core/home.html', context)
