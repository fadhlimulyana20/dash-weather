
# import multiprocessing

# # Number of workers (3 in this case, can be adjusted)
# workers = 2

# # Worker class (default 'sync' is often sufficient)
# worker_class = 'sync'

# # Number of worker connections (default should be fine for most cases)
# worker_connections = 1000

# # Timeout for workers (30 seconds is a common choice)
# timeout = 30

# # Bind to 0.0.0.0:8000 to be accessible from outside the container
# bind = '0.0.0.0:8000'

# # Preload application (use cautiously with limited memory)
# preload_app = False

import multiprocessing

bind = "0.0.0.0:8000"  # Adjust if needed
workers = 3  # Typically 2 * CPUs + 1
worker_class = "gevent"  # Async workers for I/O-heavy tasks
timeout = 120 # Adjust based on request load
loglevel = "info"

max_requests = 100
max_requests_jitter = 50

# preload_app = True

graceful_timeout = 30

# worker_class = "gthread"  # Good for handling multiple requests per worker
# threads = 4  # Increase to handle more concurrent requests per worker
# loglevel = 'error'
# timeout = 120  # Increase timeout if needed for long requests
# keepalive = 5  # Keep connections alive for 5 seconds