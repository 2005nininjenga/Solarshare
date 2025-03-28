from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        "message": "Welcome to SolarShare API 🌞",
        "endpoints": [
            "/admin/",
            "/api/auth/",
            "/api/billing/",
            "/api/plans/",
            "/api/usage/",
            "/api/payment/",
            "/api/notifications/",
            "/api/subscriptions/",
            "/api/support/",
            "/api/token/",
            "/api/token/refresh/"
        ]
    }, json_dumps_params={"ensure_ascii":False})

urlpatterns = [
    path('', root_view),  
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
    path('api/billing/', include('apps.billing.urls')),
    path('api/plans/', include('apps.plans.urls')),
    path('api/usage/', include('apps.usage.urls')),
    path('api/payment/', include('apps.payment.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/subscriptions/', include('apps.subscriptions.urls')),
    path('api/support/', include('apps.support.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
