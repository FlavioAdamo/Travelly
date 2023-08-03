## Important note:
On first docker-compose launch, your terminal could tell you:
```bash
travelly_server    |   File "/usr/local/lib/python3.8/dist-packages/psycopg2/__init__.py", line 122, in connect
travelly_server    |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
travelly_server    | django.db.utils.OperationalError: connection to server at "database" (172.20.0.2), port 5432 failed: Connection refused
travelly_server    | 	Is the server running on that host and accepting TCP/IP connections?
```

To fix those erros just stop it and relaunch `docker-compose up`