from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
 
class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=100)
    collection_id = models.CharField(max_length=100)
    collection_added = models.DateField(blank=True, null=True)
    collection_ad_group = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.collection_name
 
 
class Workflow(models.Model):
    workflow_name = models.CharField(max_length=100)
    workflow_id = models.CharField(max_length=100)
    colid = models.ForeignKey(Collection,on_delete=CASCADE)

    def __str__(self):
        return self.workflow_name

class DecomRequest(models.Model):
    collection_name = models.CharField(max_length=100)
    workflow_name = models.CharField(max_length=100)
    workflow_id = models.CharField(max_length=100)

    def __str__(self):
        return self.collection_name
