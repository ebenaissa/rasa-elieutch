FROM rasa/rasa:1.9.3
USER root
RUN python -m pip install gspread oauth2client

ADD app /app
RUN chmod +x /app/start_services.sh
ADD server.sh /app/server.sh
ADD . /app

RUN rasa train
ENTRYPOINT ["/app/server.sh"]