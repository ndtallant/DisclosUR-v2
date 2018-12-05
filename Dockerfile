# Dockerfile for DisclosUR
FROM python:3.7
LABEL maintainer "Nick Tallant <ndtallant@gmail.com>"

# Flask app setup
COPY . / 
WORKDIR /
RUN pip install -r requirements.txt 
ENV FLASK_ENV=docker
EXPOSE 5000

CMD ["python", "flask_site/app.py"]
# FROM postgres:10.6
