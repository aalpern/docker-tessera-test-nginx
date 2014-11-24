import os

DEBUG = True
GRAPHITE_URL     = os.getenv('GRAPHITE_URL', 'http://localhost:8080')
SECRET_KEY       = os.getenv('SECRET_KEY', '00761ebf-699a-8ea3-adaa-e978aaca4837')
SERVER_PORT      = 5000
SERVER_ADDRESS   = '0.0.0.0'
APPLICATION_ROOT = '/tessera'
DEFAULT_THEME    = 'solarized-dark'
