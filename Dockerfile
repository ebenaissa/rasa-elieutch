FROM rasa/rasa:1.9.3
USER root
RUN python -m pip install gspread oauth2client

ADD app /app
ADD . /app

RUN chmod +x /app/server.sh
ADD server.sh /app/server.sh
RUN chmod -R 777 /app
USER 1001


RUN rasa train
ENTRYPOINT ["/app/server.sh"]