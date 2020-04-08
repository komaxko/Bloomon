FROM python:3.7-slim-stretch

ARG python_version=3.7
ARG user_name=app_user
ARG user_home=/home
ARG app_dir=${user_home}/app

COPY . / ${app_dir}/
WORKDIR ${app_dir}

RUN useradd -Ms /bin/bash ${user_name} \
    && chown -R ${user_name} ${user_home}

USER ${user_name}
WORKDIR ${app_dir}
