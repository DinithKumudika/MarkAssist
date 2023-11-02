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

# mongodb config
# ENV MONGO_URI=mongodb+srv://dinesh1234:dinesh1234@cluster1ppmarking.atlefpe.mongodb.net/
# ENV DB_NAME=test


# google OAuth
ENV GOOGLE_CLIENT_ID=942322700321-9rl62tgmimdev1g8ko44c35djemg7dem.apps.googleusercontent.com
ENV GOOGLE_CLIENT_SECRET=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

# firebase config 
# ENV API_KEY=AIzaSyAijhFV9Y2hKxOfZsikHfQyXPE-eSRwKZg
# ENV AUTH_DOMAIN=papermarkin.firebaseapp.com
# ENV PROJECT_ID=papermarkin
# ENV STORAGE_BUCKET=papermarkin.appspot.com
# ENV MESSAGING_SENDER_ID=529261970661
# ENV APP_ID=1:529261970661:web:7b9e613f7d71e0cf1d800c
# ENV MEASUREMENT_ID=G-852GDJS8LT

# openAI config
# ENV OPENAI_API_KEY=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

#mail config

ENV MAIL_USERNAME=markassistlk@gmail.com
# MAIL_PASSWORD=markassist@1234
ENV MAIL_PASSWORD=tjgfpbkklhyhicvg
ENV MAIL_FROM=markassistlk@gmail.com
ENV MAIL_PORT=587
ENV MAIL_SERVER=smtp.gmail.com
ENV MAIL_FROM_NAME=MarkAssist
ENV MAIL_STARTTLS=True
ENV MAIL_SSL_TLS=False

# azure config
# ENV AZURE_API_KEY=1a0eabe69a514bada1badecefe5266ab
# ENV AZURE_ENDPOINT=https://markassist.cognitiveservices.azure.com/

EXPOSE 8000

CMD ["python", "src/run.py"]
