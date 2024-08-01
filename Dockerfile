FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y \
    git \
    jq \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /test

COPY . /test

RUN pip install -r /test/tests/requirements.txt

WORKDIR /test

CMD ["/bin/bash", "-c", "ci-scripts/test.sh"]
