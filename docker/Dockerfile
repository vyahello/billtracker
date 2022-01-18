FROM vyahello/billstracker-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for billstracker application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ENV CODE_DIR="/app" \
    IMAGE_REPO="vyahello/billtracker" \
    SERVER_PORT=6543 \
    IMAGE_VERSION=${VERSION}
WORKDIR ${CODE_DIR}
COPY billtracker billtracker
COPY README.md CHANGELOG.md requirements.txt requirements-dev.txt development.ini setup.py docker/entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/app/entry.sh"]
