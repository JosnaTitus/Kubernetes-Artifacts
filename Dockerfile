FROM python3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirement.txt
CMD ["python", "/app/app.py"]
