FROM python:3.12-slim
COPY code/export-to-mongo.py /

# Install required dependencies
RUN pip install requests pymongo

CMD ["python", "./export-to-mongo.py"]
