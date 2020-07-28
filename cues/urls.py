from rest_framework.routers import DefaultRouter
from . import views

app_name = "cues"
router = DefaultRouter()
router.register("", views.CueViewSet)

urlpatterns = router.urls