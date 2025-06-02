# syntax=docker/dockerfile:1
#FROM openjdk:11-bullseye
FROM openjdk:11-jre

ENV METASTORE_HADOOP_VERSION=3.2.0
ENV METASTORE_VERSION=3.0.0
ENV HADOOP_HOME=/opt/hadoop
ENV HIVE_HOME=/opt/metastore
ENV BIN_DIR=/usr/bin

ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV INSTALL_DIR=/tmp/install
ENV DATABASE_DRIVER=org.postgresql.Driver
ENV DATABASE_TYPE_JDBC=postgresql

RUN mkdir -p ${HADOOP_HOME} ${HIVE_HOME} ${MINIO_HOME}/bin ${INSTALL_DIR}


WORKDIR ${INSTALL_DIR}

# Install AWS CLI
RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm awscliv2.zip \
    && rm -rf aws/
# Download and install haddop for metastore 
RUN curl https://archive.apache.org/dist/hadoop/common/hadoop-${METASTORE_HADOOP_VERSION}/hadoop-${METASTORE_HADOOP_VERSION}.tar.gz -Lo hadoop.tgz \
    && tar xvzf hadoop.tgz --directory ${HADOOP_HOME} --strip-components 1 \
    && rm hadoop.tgz
# Download and install Hive metastore
RUN curl https://downloads.apache.org/hive/hive-standalone-metastore-${METASTORE_VERSION}/hive-standalone-metastore-${METASTORE_VERSION}-bin.tar.gz -Lo hive.tgz \
    && tar xvzf hive.tgz --directory ${HIVE_HOME} --strip-components 1 \
    && rm hive.tgz
# Download and install Postgres deiver for Hive metastore
RUN curl https://repo1.maven.org/maven2/org/postgresql/postgresql/42.4.0/postgresql-42.4.0.jar -Lo pgsql.jar \
    && mv pgsql.jar ${HIVE_HOME}/lib 

# Download Java AWS SDK
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.17.247/bundle-2.17.247.jar -Lo bundle-2.17.247.jar \
    && mv bundle-2.17.247.jar ${HIVE_HOME}/lib
# Download URL connection client required for S3FileIO
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/url-connection-client/2.17.247/url-connection-client-2.17.247.jar -Lo url-connection-client-2.17.247.jar \
     && mv url-connection-client-2.17.247.jar ${HIVE_HOME}/lib

WORKDIR ${HIVE_HOME}

COPY metastore-site.xml ${HIVE_HOME}/conf
COPY entrypoint.sh ${BIN_DIR}

RUN chmod u+x ${HIVE_HOME}/bin/*

EXPOSE 9083


ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["notebook"]




# FROM amazoncorretto:8u442-alpine3.21-jre

# ARG HADOOP_VERSION=3.4.1
# ARG HIVE_METASTORE_VERSION=3.0.0
# ARG POSTGRES_CONNECTOR_VERSION=42.7.2
# ARG AWS_SDK_VERSION=1.12.367
# ARG ICEBERG_VERSION=1.3.1
# ARG AVRO_VERSION=1.11.4
# ARG AWS_SDK_V2_VERSION=2.22.0

# WORKDIR /app
# #SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# # hadolint ignore=DL3008
# RUN apk update && apk upgrade && apk add net-tools gettext curl

# RUN echo "Download and extract the Hadoop binary package" && \
#     curl https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz \
#     | tar xvz -C /opt/ && \
#     ln -s /opt/hadoop-$HADOOP_VERSION /opt/hadoop && \
#     rm -r /opt/hadoop/share/doc

# RUN echo "Download and install the standalone metastore binary" && \
#     curl https://downloads.apache.org/hive/hive-standalone-metastore-$HIVE_METASTORE_VERSION/hive-standalone-metastore-$HIVE_METASTORE_VERSION-bin.tar.gz \
#     | tar xvz -C /opt/ && \
#     ln -s /opt/apache-hive-metastore-$HIVE_METASTORE_VERSION-bin /opt/hive-metastore

# RUN echo "Fix 'java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument'" && \
#     echo "Keep this until this lands: https://issues.apache.org/jira/browse/HIVE-22915" && \
#     rm /opt/apache-hive-metastore-$HIVE_METASTORE_VERSION-bin/lib/guava-19.0.jar && \
#     cp /opt/hadoop-$HADOOP_VERSION/share/hadoop/hdfs/lib/guava-27.0-jre.jar /opt/apache-hive-metastore-$HIVE_METASTORE_VERSION-bin/lib/

# RUN echo "Download and install the database connector" && \
#     curl -L https://jdbc.postgresql.org/download/postgresql-$POSTGRES_CONNECTOR_VERSION.jar --output /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar && \
#     ln -s /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar /opt/hadoop/share/hadoop/common/lib/ && \
#     ln -s /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar /opt/hive-metastore/lib/

# # 添加 hadoop-aws JAR（包含 S3AFileSystem 實現）
# RUN echo "Download and install hadoop-aws" && \
#     curl -L https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/$HADOOP_VERSION/hadoop-aws-$HADOOP_VERSION.jar --output /opt/hadoop-aws-$HADOOP_VERSION.jar && \
#     ln -s /opt/hadoop-aws-$HADOOP_VERSION.jar /opt/hadoop/share/hadoop/common/lib/ && \
#     ln -s /opt/hadoop-aws-$HADOOP_VERSION.jar /opt/hive-metastore/lib/

# # 添加 AWS SDK v1 支持
# RUN echo "Download and install AWS S3 v1 support" && \
#     curl -L https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar --output /opt/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar && \
#     ln -s /opt/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar /opt/hadoop/share/hadoop/common/lib/ && \
#     ln -s /opt/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar /opt/hive-metastore/lib/

# # 添加 AWS SDK v2 核心組件
# RUN echo "Download and install AWS SDK v2 core components" && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/sdk-core/${AWS_SDK_V2_VERSION}/sdk-core-${AWS_SDK_V2_VERSION}.jar --output /opt/sdk-core-${AWS_SDK_V2_VERSION}.jar && \
#     ln -s /opt/sdk-core-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/

# # 添加 AWS SDK v2 S3 client
# RUN echo "Download and install AWS SDK v2 S3 client" && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/s3/${AWS_SDK_V2_VERSION}/s3-${AWS_SDK_V2_VERSION}.jar --output /opt/s3-${AWS_SDK_V2_VERSION}.jar && \
#     ln -s /opt/s3-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/

# # 添加必要的依賴項
# RUN echo "Download and install AWS SDK v2 dependencies" && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/auth/${AWS_SDK_V2_VERSION}/auth-${AWS_SDK_V2_VERSION}.jar --output /opt/auth-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/http-client-spi/${AWS_SDK_V2_VERSION}/http-client-spi-${AWS_SDK_V2_VERSION}.jar --output /opt/http-client-spi-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/regions/${AWS_SDK_V2_VERSION}/regions-${AWS_SDK_V2_VERSION}.jar --output /opt/regions-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/utils/${AWS_SDK_V2_VERSION}/utils-${AWS_SDK_V2_VERSION}.jar --output /opt/utils-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/http-auth-spi/${AWS_SDK_V2_VERSION}/http-auth-spi-${AWS_SDK_V2_VERSION}.jar --output /opt/http-auth-spi-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/apache-client/${AWS_SDK_V2_VERSION}/apache-client-${AWS_SDK_V2_VERSION}.jar --output /opt/apache-client-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/aws-core/${AWS_SDK_V2_VERSION}/aws-core-${AWS_SDK_V2_VERSION}.jar --output /opt/aws-core-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/metrics-spi/${AWS_SDK_V2_VERSION}/metrics-spi-${AWS_SDK_V2_VERSION}.jar --output /opt/metrics-spi-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/profiles/${AWS_SDK_V2_VERSION}/profiles-${AWS_SDK_V2_VERSION}.jar --output /opt/profiles-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/third-party-jackson-core/${AWS_SDK_V2_VERSION}/third-party-jackson-core-${AWS_SDK_V2_VERSION}.jar --output /opt/third-party-jackson-core-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/annotations/${AWS_SDK_V2_VERSION}/annotations-${AWS_SDK_V2_VERSION}.jar --output /opt/annotations-${AWS_SDK_V2_VERSION}.jar && \
#     curl -L https://repo1.maven.org/maven2/software/amazon/awssdk/json-utils/${AWS_SDK_V2_VERSION}/json-utils-${AWS_SDK_V2_VERSION}.jar --output /opt/json-utils-${AWS_SDK_V2_VERSION}.jar && \
#     ln -s /opt/auth-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/http-client-spi-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/regions-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/utils-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/http-auth-spi-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/apache-client-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/aws-core-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/metrics-spi-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/profiles-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/third-party-jackson-core-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/annotations-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/ && \
#     ln -s /opt/json-utils-${AWS_SDK_V2_VERSION}.jar /opt/hive-metastore/lib/

# RUN echo "Download and install Iceberg for Trino 475" && \
#     curl -L https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-hive-runtime/$ICEBERG_VERSION/iceberg-hive-runtime-$ICEBERG_VERSION.jar --output /opt/iceberg-hive-runtime-$ICEBERG_VERSION.jar && \
#     ln -s /opt/iceberg-hive-runtime-$ICEBERG_VERSION.jar /opt/hive-metastore/lib/

# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/jackson-databind-2.9.4.jar
# RUN echo "Download and install the database connector" && \
#     curl -L https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.9.6/jackson-databind-2.9.7.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/jackson-databind-2.9.7.jar

# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/derby-10.10.2.0.jar
# RUN echo "Download and install the database connector" && \
#     curl -L https://repo1.maven.org/maven2/org/apache/derby/derby/10.14.3/derby-10.14.3.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/derby-10.14.3.jar

# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-1.2-api-2.8.2.jar
# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-api-2.8.2.jar
# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-core-2.8.2.jar
# RUN rm /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-slf4j-impl-2.8.2.jar
# RUN echo "Download and install the database connector" && \
#     curl -L https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-1.2-api/2.16.0/log4j-1.2-api-2.16.0.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-1.2-api-2.16.0.jar && \
#     curl -L https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.16.0/log4j-api-2.16.0.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-api-2.16.0.jar && \
#     curl -L https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.16.0/log4j-core-2.16.0.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-core-2.16.0.jar && \
#     curl -L https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-slf4j-impl/2.16.0/log4j-slf4j-impl-2.16.0.jar --output /opt/apache-hive-metastore-3.0.0-bin/lib/log4j-slf4j-impl-2.16.0.jar

# RUN rm /opt/hadoop-3.4.1/share/hadoop/hdfs/lib/avro-1.9.2.jar
# RUN rm /opt/hadoop-3.4.1/share/hadoop/common/lib/avro-1.9.2.jar
# RUN echo "Download and install the database connector" && \
#     curl -L https://repo1.maven.org/maven2/org/apache/avro/avro/1.11.4/avro-1.11.4.jar --output /opt/hadoop-3.4.1/share/hadoop/hdfs/lib/avro-1.9.2.jar && \
#     curl -L https://repo1.maven.org/maven2/org/apache/avro/avro/1.11.4/avro-1.11.4.jar --output /opt/hadoop-3.4.1/share/hadoop/common/lib/avro-1.9.2.jar

# RUN rm /opt/hadoop-3.4.1/share/hadoop/yarn/timelineservice/lib/htrace-core-3.1.0-incubating.jar
# RUN rm /opt/hadoop-3.4.1/share/hadoop/client/hadoop-client-runtime-3.4.1.jar
# RUN rm /opt/hadoop-3.4.1/share/hadoop/yarn/hadoop-yarn-applications-catalog-webapp-3.4.1.war

# RUN apk add --no-cache bash

# COPY hive-site.xml hive-site_TEMPLATE.xml
# COPY metastore-site.xml metastore-site_TEMPLATE.xml
# COPY --chmod=755 run.sh run.sh

# ENV HADOOP_HOME="/opt/hadoop"
# ENV PATH="/opt/hadoop/bin:${PATH}"
# ENV METASTORE_PORT=9083

# ENV DATABASE_TYPE=postgres
# # ENV DATABASE_PORT=5432
# # ENV DATABASE_USER=admin
# # ENV DATABASE_PASSWORD=pass
# # ENV DATABASE_DB=metastore
# # ENV DATABASE_HOST=metastore-db

# CMD [ "./run.sh" ]
# HEALTHCHECK CMD [ "sh", "-c", "netstat -ln | grep 9083" ]