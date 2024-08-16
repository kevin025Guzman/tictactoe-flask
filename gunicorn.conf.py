# Gunicorn conf file
bind = '0.0.0.0:10000'
# Maximum time (in seconds) a worker is allowed to process a request
timeout = 6000
# Number of worker processes to spawn
# workers = 4
# Number of threads to be used per worker
threads = 4
# Maximum number of simultaneous clients that a single worker can handle
worker_connections = 1000
# Worker class to use (in this case, using eventlet)
worker_class = 'eventlet'