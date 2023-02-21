from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Collection, Workflow, DecomRequest
from django.core import serializers
import json

# This is the homepage view
def index(request):
    return HttpResponse("Homepage")
 

# This view handles the decommission request form submission
def decom_request(request):
    if request.method == 'POST':
        # Get the collection and workflow IDs and names from the form data
        collection_id = request.POST.get('collection')
        workflow_id = request.POST.get('workflow')
        collection_name = Collection.objects.get(id=collection_id).collection_name
        workflow = Workflow.objects.get(colid=collection_id, id=workflow_id)
        workflow_name = workflow.workflow_name
        workflow_id = workflow.workflow_id

        # Create a new DecomRequest object with the collection and workflow data
        decom_request = DecomRequest(collection_name=collection_name, workflow_name=workflow_name, workflow_id=workflow_id)
        decom_request.save()

        # Redirect the user to the decommission request page
        return redirect('decom_request')

    # If the request method is not POST, render the decommission request form
    template_name = 'decom_request.html'
    colcontext = Collection.objects.all()
    workcontext = Workflow.objects.all()    
 
    return render(request, template_name, {'Collection': colcontext, 'Workflow': workcontext})


# This view returns the list of workflows for a given collection ID in JSON format
def get_workflows(request, collection_id):
    workflows = Workflow.objects.filter(colid=collection_id).values('id', 'workflow_name', 'workflow_id')
    return JsonResponse(list(workflows), safe=False)
