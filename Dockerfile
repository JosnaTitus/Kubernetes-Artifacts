FROM python:3.7
ADD webapp.py /docker-entrypoint-initdb.d
EXPOSE 8080 
