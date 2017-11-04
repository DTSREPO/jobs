from django.shortcuts import render, redirect
from django.views import View
from employer_app import models as EmpModels
from jobpost_app import models as JobModels


# Create your views here.

class JobPostCrud(View):
    template = 'employer_app/job_post_form.html'
    try:
        emp = EmpModels.Employer.objects.get(pk=1)
    except EmpModels.Employer.DoesNotExist:
        emp = None

    def get(self, request, job_id=None):
        industries = JobModels.Industry.objects.all()
        categories = JobModels.Category.objects.all()
        locations = JobModels.Location.objects.all()

        if job_id:
            job_id = int(job_id)
            jobpost = EmpModels.JobPost.objects.get(pk=job_id)
            context = {
                'title': 'Create or Update Job Post',
                'emp': self.emp,
                'industries': industries,
                'categories': categories,
                'locations': locations,
                'jobpost': jobpost
            }

        else:
            context = {
                'title': 'Create or Update Job Post',
                'emp': self.emp,
                'industries': industries,
                'categories': categories,
                'locations': locations
            }

        return render(request, self.template, context)

    def post(self, request, job_id=None):
        industries = JobModels.Industry.objects.all()
        categories = JobModels.Category.objects.all()
        locations = JobModels.Location.objects.all()

        com_id = request.POST.get('com-id', '')
        category = request.POST.get('category', '')
        industry = request.POST.get('industry', '')
        job_title = request.POST.get('job-title', '')
        vacancies = request.POST.get('vacancies', '')
        attach_photo = request.POST.get('attach-photo', False)
        apply_ins = request.POST.get('apply-ins', '')

        last_date = request.POST.get('deadline','')

        age_frm = request.POST.get('age-frm', '')
        age_to = request.POST.get('age-to', '')
        gender = request.POST.get('gender', '')

        # job_types = request.POST.getlist('job-type')
        # job_level = request.POST.getlist('job-level')

        edu_qlf = request.POST.get('edu-qlf', '')
        job_context = request.POST.get('job-context', '')
        job_resp = request.POST.get('job-resp', '')
        adtn_job_req = request.POST.get('adn-req', '')
        exp_type = request.POST.get('exp-type', '')
        exp_min = request.POST.get('min-exp', '')
        exp_max = request.POST.get('max-exp', '')
        location = request.POST.get('location', '')  # foreign
        salary_range_type = request.POST.get('sal-range-type', '')
        salary_min = request.POST.get('min-sal', '')
        salary_max = request.POST.get('max-sal', '')
        other_benefits = request.POST.get('other-benifits', '')
        excl_job_flag = request.POST.get('excl-job', False)

        if job_id:
            job_id = int(job_id)
            jobpost = EmpModels.JobPost.objects.get(pk=job_id)

            jobpost.company_id = com_id
            jobpost.category_id = category
            jobpost.industry_id = industry
            jobpost.job_title = job_title
            jobpost.vacancies = vacancies
            jobpost.with_photo = attach_photo
            jobpost.apply_ins = apply_ins

            #jobpost.last_date = last_date

            jobpost.age_range_form = age_frm
            jobpost.age_range_to = age_to
            jobpost.gender = gender

            # jobpost.job_type = job_types
            # jobpost.job_level = job_level

            jobpost.edu_qualification = edu_qlf
            jobpost.job_context = job_context
            jobpost.job_resp = job_resp
            jobpost.adtn_job_req = adtn_job_req
            jobpost.exp_type = exp_type
            jobpost.exp_min = exp_min
            jobpost.exp_max = exp_max
            jobpost.location_id = location
            jobpost.salary_range_type = salary_range_type
            jobpost.salary_min = salary_min
            jobpost.salary_max = salary_max
            jobpost.other_benefits = other_benefits
            jobpost.excl_job_flag = excl_job_flag

            jobpost.save()

            context = {
                'title': 'Create or Update Job Post',
                'emp': self.emp,
                'industries': industries,
                'categories': categories,
                'locations': locations,
                'jobpost': jobpost,
                'msg': 'Job Updated!'
            }
            # return render(request, self.template, context)

        else:
            jobpost = EmpModels.JobPost(
                company_id=com_id,
                category_id=category,
                industry_id=industry,
                job_title=job_title,
                vacancies=vacancies,
                with_photo=attach_photo,
                apply_ins=apply_ins,

                #last_date=last_date,

                age_range_form=age_frm,
                age_range_to=age_to,
                gender=gender,
                edu_qualification=edu_qlf,
                job_context=job_context,
                job_resp=job_resp,
                adtn_job_req=adtn_job_req,
                exp_type=exp_type,
                exp_min=exp_min,
                exp_max=exp_max,
                location=location,
                salary_range_type=salary_range_type,
                salary_min=salary_min,
                salary_max=salary_max,
                other_benefits=other_benefits,
                excl_job_flag=excl_job_flag
            )
            jobpost.save()

            # jobpost.job_type.add(*job_types)
            # jobpost.job_level.add(*job_level)

            context = {
                'title': 'Create or Update Job Post',
                'emp': self.emp,
                'industries': industries,
                'categories': categories,
                'locations': locations,
                'jobpost': jobpost,
                'msg': 'New Job Inserted!'
            }

        return redirect("employer_app:job-post", jobpost.id)