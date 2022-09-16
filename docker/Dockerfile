FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# SHELL OUTPUT when running docker build
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

# Using pip to install from requirements.txt failed. Gunicorn was not installing properly. Maybe the above warning 
# has something to do with that.

# Installing them one by one like this works.
# COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir amqp \
    #&& pip install asgiref \
    #&& pip install billiard \
    #&& pip install celery \
    #&& pip install click \
    #&& pip install click-didyoumean \
    #&& pip install click-plugins \
    #&& pip install click-repl \
    && pip install Django \
    #&& pip install django-celery-beat \
    # See https://stackoverflow.com/questions/67409452/gunicorn-importerror-cannot-import-name-already-handled-from-eventlet-wsgi
    && pip install eventlet==0.33.0 https://github.com/benoitc/gunicorn/archive/refs/heads/master.zip#egg=gunicorn==20.1.0 \
    && pip install gunicorn \
    && pip install pymysql \
    && pip install pyyaml \
    && pip install Pillow \
    && pip install django-cookie-consent \
    && pip install djangorestframework \
    && pip install django-widget-tweaks \
    && pip install django-modeltranslation \
    #&& pip install kombu \
    #&& pip install prompt-toolkit \
    #&& pip install psycopg2 \
    #&& pip install pytz \
    #&& pip install redis \
    #&& pip install six \
    #&& pip install sqlparse \
    #&& pip install vine \
    #&& pip install wcwidth \
    # && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static 
    # && export PATH="$PATH:${$(which gunicorn)/gunicorn/}"

WORKDIR /app
COPY  . .
RUN chmod +x docker/*.sh \
    && chown -R app_user:app_user .
USER app_user:app_user

ENTRYPOINT [ "docker/entrypoint.sh" ]
CMD [ "docker/start.sh", "server" ]
#RUN venv/bin/gunicorn \
#    --bind 0.0.0.0:8000 \
#    --workers 2 \
#    --worker-class eventlet \
#    --log-level DEBUG \
#    --access-logfile "-" \
#    --error-logfile "-" \
#    smartestate.wsgi
