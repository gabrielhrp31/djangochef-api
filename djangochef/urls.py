"""djangochef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, re_path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from djangochef.Views.RecipesListChef import RecipesListChef
from djangochef.Views.chef_auth.ChefCreate import ChefCreate
from djangochef.Views.chef_auth.RecipeChefDetail import RecipeChefDetail
from djangochef.Views.chef_auth.RecipeChefCreate import RecipeChefCreate
from djangochef.Views.RecipeFilter import RecipeFilter
from djangochef.Views.RecipeDetail import RecipeDetail

urlpatterns = [
    # chef login routes
    path('login/', obtain_jwt_token, name='login'),
    url(r'^refresh-token/', refresh_jwt_token, name='token_refresh'),

    # chef creation route
    path('chef/', ChefCreate.as_view(), name="chef"),

    # chef protected routes
    path('chef/recipe/', RecipeChefCreate.as_view(), name="chef_recipe_create"),
    path('chef/recipe/<int:pk>/', RecipeChefDetail.as_view(), name="chef_recipe_edit"),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name="recip_get"),

    # user public routes
    path('recipes/chef/<int:pk>/', RecipesListChef.as_view(), name="recip_list_chef"),
    re_path(r'^recipe$', RecipeFilter.as_view(), name="recip_filter"),
    path('docs/', include_docs_urls(title='DjangoChef API', public=False))
]
