# Snapshot Migration Using Spark on Kubernetes

## Building a docker container with the PySpark file for the Snapshot Migration Job

1.  docker build -f Dockerfile --tag pyspark_migration_snapshot .
2. docker tag pyspark_migration_snapshot:latest asia.gcr.io/gcp-project-demo/pyspark_migration_snapshot:1.0.0
3. docker push asia.gcr.io/gcp-project-demo/pyspark_migration_snapshot:1.0.0