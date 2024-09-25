from django.contrib import admin
from django.urls import path
from blog.views import menu_view, blog_single
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomePage, name='Home'),
    path('', menu_view, name='menu'),
    path('blog-single/', blog_single, name='blog_single'),
    # path('skew-star/', Skew_star_view, name='skew_star_view'),
    # path('about/', about_view, name='about_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
