from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Collection, Workflow, DecomRequest
from django.core import serializers
import json

def index(request):
    return HttpResponse("Homepage")
 

# def decom_request(request):
#     if request.method == 'POST':
#         collection_id = request.POST.get('collection')
#         workflow_id = request.POST.get('workflow')
#         collection_name = Collection.objects.get(id=collection_id).collection_name
#         workflow_name = Workflow.objects.get(colid=collection_id, id=workflow_id).workflow_name
#         decom_request = DecomRequest(collection_name=collection_name, workflow_name=workflow_name)
#         decom_request.save()
#         return redirect('decom_request')

#     template_name = 'decom_request.html'
#     colcontext = Collection.objects.all()
#     workcontext = Workflow.objects.all()    
 
#     return render(request, template_name, {'Collection': colcontext, 'Workflow': workcontext})

def decom_request(request):
    if request.method == 'POST':
        collection_id = request.POST.get('collection')
        workflow_id = request.POST.get('workflow')
        collection_name = Collection.objects.get(id=collection_id).collection_name
        workflow = Workflow.objects.get(colid=collection_id, id=workflow_id)
        workflow_name = workflow.workflow_name
        workflow_id = workflow.workflow_id
        decom_request = DecomRequest(collection_name=collection_name, workflow_name=workflow_name, workflow_id=workflow_id)
        decom_request.save()
        return redirect('decom_request')

    template_name = 'decom_request.html'
    colcontext = Collection.objects.all()
    workcontext = Workflow.objects.all()    
 
    return render(request, template_name, {'Collection': colcontext, 'Workflow': workcontext})






def get_workflows(request, collection_id):
    workflows = Workflow.objects.filter(colid=collection_id).values('id', 'workflow_name', 'workflow_id')
    return JsonResponse(list(workflows), safe=False)


