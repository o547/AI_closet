from django.urls import path
from . import views
app_name="closet"
urlpatterns=[
    path("",views.index,name="index"),
    path("garment/resistor",views.garment_resistor,name="garment_resistor"),
    path("garment/list",views.garment_list,name="garment_list"),
    path("garment/delete/<uuid:id>",views.garment_delete,name="garment_delete"),
    path("coordinate/register",views.coordinate_register,name="coordinate_register"),
    path("coordinate/list",views.coordinate_list,name="coordinate_list"),
    path("coordinate/delete/<uuid:id>",views.coordinate_delete,name="coordinate_delete"),
    path("coordinate/evaluation/<uuid:id>",views.ai_evaluation,name="ai_evaluation"),
    path("garment/ai_coordinate",views.ai_coordinate,name="ai_coordinate"),


]