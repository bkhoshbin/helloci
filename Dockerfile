FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install Flask prometheus-client pytest requests
EXPOSE 5000
CMD ["python", "app.py"]
