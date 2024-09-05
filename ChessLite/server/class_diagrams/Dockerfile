FROM openjdk:11

RUN apt-get update && apt-get install -y graphviz && apt-get clean

WORKDIR /usr/src/diagrams
COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]