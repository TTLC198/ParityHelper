## Deployment

### Configure values

Be sure you set the port and address in [docker-compose.yaml](/docker-compose.yaml)

Configure app
```yaml
      TG_TOKEN: ""           # your TG Bot token
      DB_HOST: pg            # your TG Bot token
      DB_PORT: 5432          # your TG Bot token
      DB_NAME: postgres      # postgres database name
      DB_USER: postgres      # postgres user name
      DB_PASS: password      # postgres password
```

Configure postgres db
```yaml
      POSTGRES_DB: postgres         # postgres database name
      POSTGRES_USER: postgres       # postgres user name
      POSTGRES_PASSWORD: password   # postgres password
```

### Building
```sh
docker compose build 
```

### Start

```sh
docker compose up -d
```

### Stop
```sh
docker compose down
```