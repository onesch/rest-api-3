from rest_framework import routers

from app.orders.views import OrderViewSet


router = routers.DefaultRouter()
router.register(r"orders", OrderViewSet)

urlpatterns = router.urls
