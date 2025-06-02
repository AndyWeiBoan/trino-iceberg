#### postgresql

```sh
docker run -d --name pgadmin -p 5080:80 -e PGADMIN_DEFAULT_EMAIL=pgadmin@test.com -e PGADMIN_DEFAULT_PASSWORD=Sa12345678 dpage/pgadmin4
```

```sh
docker run -d --name postgresql -p 5432:5432 -e POSTGRES_PASSWORD="Sa12345678"  postgres:15.4
```

#### metastore

```sh
docker build -f metastore/hive-metastore/docker/Dockerfile -t hive-metastore-pgsql:test ./metastore/hive-metastore/docker
```

```sh
helm upgrade --install metastore getindata-hms/hive-metastore -f metastore/hive-metastore/hive-metastore/values.yaml -f metastore/hive-metastore/hive-metastore/dev.yaml --version 0.1.0
```

#### minio

```sh
helm repo add minio https://charts.min.io/ && \
helm repo update minio && \
helm upgrade --install minio minio/minio -f minio/values.yaml -f minio/custom.yaml --version 5.4.0
```

#### trino

```sh
helm repo add trino https://trinodb.github.io/helm-charts || true && \
helm upgrade --install trino trino/trino -f trino/charts/trino/values.yaml -f trino/charts/trino/dev.yaml --version 1.39.0 
```