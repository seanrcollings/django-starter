from libs.path import pack_routes

# Adding a new route requires a server restart
urlpatterns = pack_routes("client")
