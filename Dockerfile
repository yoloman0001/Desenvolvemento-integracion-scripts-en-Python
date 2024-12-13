FROM python:3.12-slim
COPY code/export-to-mongo.py /

# Install required dependencies
RUN pip install requests pymongo

# Expose the port of MongoDB
EXPOSE 27017

CMD ["python", "./export-to-mongo.py"]
