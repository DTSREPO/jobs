from django.shortcuts import render
from employer_app.models import JobPost, Employer
from jobpost_app.models import Category


def cat_job_list(request, cat_id=None):
    if cat_id:
        cat_id = int(cat_id)
        category = Category.objects.get(pk=cat_id)
        jobpost = JobPost.objects.filter(category_id=cat_id)
        companies = Employer.objects.all()
        template = "jobpost_app/frontend/cat_job_list.html"
        context = {'title': 'Category Wise Job List', 'companies': companies, 'category': category, 'jobpost': jobpost}

    return render(request, template, context)
