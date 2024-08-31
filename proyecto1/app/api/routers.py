from rest_framework.routers import DefaultRouter
from ..libro.views import *
from ..autor.views import *
from ..genero.views import *

router = DefaultRouter()

router.register(r'libro', StateViewset, basename='libro')
router.register(r'autor', StateViewset, basename='autor')
router.register(r'genero', StateViewset, basename='genero')

urlpatterns = router.urls