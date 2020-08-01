FROM python

RUN apt-get update && apt-get install -y vim

RUN pip install boto3 tifffile

COPY upload_processed.py ./upload_processed.py
COPY download_raw.py ./download_raw.py
COPY process_images.py  ./process_images.py

CMD ["python3"]
