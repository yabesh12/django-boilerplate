"""naturals_bridal_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graph_api.api import schema


# django admin customization settings
admin.site.site_header = " {{ project_name }} Admin"
admin.site.site_title = " {{ project_name }} Admin Portal"
admin.site.index_title = "Welcome to {{ project_name }} Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    # graphql interface path
    re_path(r"graphql", csrf_exempt(GraphQLView.as_view(graphiql=get_bool_from_env("GRAPHIQL", False), schema=schema))),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    try:
        import debug_toolbar
    except ImportError:
        """The debug toolbar was not installed. Ignore the error.
        settings.py should already have warned the user about it."""
    else:
        urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
