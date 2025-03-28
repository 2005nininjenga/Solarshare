from rest_framework.routers import DefaultRouter
from .views import SupportTicketViewSet

router = DefaultRouter()
router.register(r'', SupportTicketViewSet)

urlpatterns = router.urls
