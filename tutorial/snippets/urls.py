from django.conf.urls import url
from snippets import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    #url('snippets/', views.snippet_list),
    #url('snippets/<int:pk>/', views.snippet_detail),
    url('snippets/', csrf_exempt(views.SnippetList.as_view())),
]