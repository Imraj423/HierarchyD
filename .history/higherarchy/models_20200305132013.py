from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class FilesandFolders(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('name', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='folder')

    class MPTTMeta:
        order_insertion_by = ['name']
