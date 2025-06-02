# minio

* Version
  * Application: RELEASE.2024-12-18T13-15-44Z
  * Chart: 5.4.0

```
helm repo add minio https://charts.min.io/
helm repo update minio
helm -n operation diff upgrade --install minio minio/minio -f values.yaml -f custom.yaml --version 5.4.0
```