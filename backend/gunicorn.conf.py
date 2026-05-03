import multiprocessing
import os

# Gunicorn configuration for Railway
bind = f"0.0.0.0:{os.environ.get('PORT', '5001')}"
workers = 1  # Keep to 1 for simplicity and memory efficiency on Railway
worker_class = "gevent"
worker_connections = 1000
timeout = 300
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Application loading
preload_app = False
