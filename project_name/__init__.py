from __future__ import absolute_import, unicode_literals
from {{ project_name }}.celery import app as celery_app

__all__ = ['celery_app']
