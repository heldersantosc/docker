FROM python:3.6
LABEL maintainer="Helder Santos"

RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log

USER www
VOLUME /log
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["C:\Users\helder.santos\AppData\Local\Programs\Python\Python38-32"]
CMD ["run.py"]