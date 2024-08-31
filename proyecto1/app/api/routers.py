from rest_framework.routers import DefaultRouter
from ..libro.views import *
from ..autor.views import *
from ..genero.views import *

router = DefaultRouter()

router.register(r'libro', LibroViewset, basename='libro')
router.register(r'autor', AutorViewset, basename='autor')
#"router.register(r'genero', GeneroViewset, basename='genero')

urlpatterns = router.urls