FROM python

ENV FLASK_APP=blackapi \
    FLASK_ENV=Development \
    FLASK_DEBUG=True

WORKDIR /app
 
COPY requirements.txt ./
 
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]