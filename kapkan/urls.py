from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.shop.urls')),
    path('cart/', include(('apps.cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('apps.orders.urls', 'orders'), namespace='orders')),
    path('accounts/', include('apps.user_reg_log.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)