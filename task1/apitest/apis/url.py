from rest_framework.routers import DefaultRouter
from apitest.apis.views import LessionListViewSet

app_name = 'lessionapis'
router = DefaultRouter()
router.register('get_title',LessionListViewSet,basename='lessionlistapi')
urlpatterns = router.urls