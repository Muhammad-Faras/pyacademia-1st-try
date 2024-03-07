from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat_view(request,group_name):
    context = {}
    group_name = 'your_group_name here'
    context['group_name'] = group_name
    return render(request, 'chat/chat_page.html',context)