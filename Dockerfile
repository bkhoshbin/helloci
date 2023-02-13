FROM python:3.8

# Set the working directory to /app
WORKDIR /app

COPY . /app
WORKDIR /app
RUN pip install Flask prometheus-client pytest requests


# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose port 80
EXPOSE 80

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
