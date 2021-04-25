FROM test
ADD webapp.py /docker-entrypoint-initdb.d
EXPOSE 8080 
