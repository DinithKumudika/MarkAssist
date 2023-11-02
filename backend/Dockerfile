ARG PYTHON_VERSION="3.11.0"
ARG APP_ROOT=/server

FROM python:${PYTHON_VERSION}

LABEL version="1.0.0"
WORKDIR ${APP_ROOT}

# Install libGL
RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install --no-cache-dir -U pip==22.3
COPY ./requirements.txt ${APP_ROOT}/requirements.txt
RUN pip install --no-cache-dir -r ${APP_ROOT}/requirements.txt

COPY ./service_account.json ${APP_ROOT}/service_account.json
COPY ./src ${APP_ROOT}/src
COPY ./data ${APP_ROOT}/data
ENV PROJECT_NAME = mark-assist-api

# server config
ENV HOST=0.0.0.0
ENV PORT=8000
ENV JWT_SECRET_KEY=5RKmHaG+TxOYHFR19yQKttEmq5WUHio3uYfIRmvxlQI=


# google OAuth
ENV GOOGLE_CLIENT_ID=942322700321-9rl62tgmimdev1g8ko44c35djemg7dem.apps.googleusercontent.com
ENV GOOGLE_CLIENT_SECRET=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

#mail config

ENV MAIL_USERNAME=markassistlk@gmail.com
ENV MAIL_PASSWORD=tjgfpbkklhyhicvg
ENV MAIL_FROM=markassistlk@gmail.com
ENV MAIL_PORT=587
ENV MAIL_SERVER=smtp.gmail.com
ENV MAIL_FROM_NAME=MarkAssist
ENV MAIL_STARTTLS=True
ENV MAIL_SSL_TLS=False


EXPOSE 8000

CMD ["python", "src/run.py"]
