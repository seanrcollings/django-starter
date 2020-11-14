from libs.path import PackRoutes

# Adding a new route requires a server restart
urlpatterns = PackRoutes("client").urls
