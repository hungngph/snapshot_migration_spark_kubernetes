FROM gcr.io/spark-operator/spark-py:v3.1.1-hadoop3

USER root:root

RUN mkdir -p /app
RUN mkdir -p /opt/hadoop/conf
RUN mkdir -p /opt/spark/conf

COPY ./spark-files  /app
COPY ./jars/mysql-connector-java-8.0.28.jar /opt/spark/jars
COPY ./jars/gcs-connector-hadoop3-2.2.17-shaded.jar /opt/spark/jars
COPY ./conf/core-site.xml /opt/hadoop/conf
COPY ./conf/spark-env.sh $SPARK_HOME/conf

WORKDIR /app

ENTRYPOINT [ "/opt/entrypoint.sh" ]