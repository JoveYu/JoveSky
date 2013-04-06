import sae
from JoveSky import wsgi

application = sae.create_wsgi_app(wsgi.application)
