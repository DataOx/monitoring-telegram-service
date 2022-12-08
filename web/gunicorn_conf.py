from multiprocessing import cpu_count

bind = '0.0.0.0:3344'
timeout = 120
workers = cpu_count()
