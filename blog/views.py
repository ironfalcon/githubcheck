from django.shortcuts import render
from django.http import JsonResponse
from .models import Post, Report


def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        try:
            entity = Report.objects.get(github_login=request.POST.get('github_login'))
        except (KeyError, Report.DoesNotExist):
            # Redisplay the question voting form.
            github_login = request.POST['github_login']
            response_data['github'] = github_login
            return JsonResponse(response_data)
        else:
            ldap = entity.ldap_login
            github = entity.github_login
            response_data['ldap'] = ldap
            response_data['github'] = github
            return JsonResponse(response_data)



    return render(request, 'main.html')    