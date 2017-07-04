FROM bizcapdev/base-python-alpine-django

ENV PACOTES build-dependencies linux-headers postgresql-dev make gcc \
  g++ ca-certificates zlib-dev jpeg-dev tiff-dev freetype-dev lcms2-dev \
  libwebp-dev tcl-dev tk-dev libxml2-dev libxslt-dev git

RUN apk update && \
  apk upgrade && \
  apk add --no-cache --virtual $PACOTES && \
  rm -rf /var/cache/apk/*

ADD requirements.txt /var/codigo/requirements.txt
WORKDIR /var/codigo

RUN pip install -r /var/codigo/requirements.txt

RUN mkdir -p /var/etc/log

EXPOSE 80

ARG VERSAO=SemVersaoConfigurada
ENV VERSAO $VERSAO

# VOLUME /var/code
# ENTRYPOINT ['/var/code/entrypoint.sh']
