from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superuser/', admin.site.urls, name="admin"),
    path('', include('shop.urls'), name='shop'),
    path('account/', include('account.urls'), name='account'),
    path('user-activity/', include('user_activity.urls'), name='UserActivity'),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
