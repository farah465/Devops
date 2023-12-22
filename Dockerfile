FROM ubuntu:latest
RUN apt-get update && apt-get install python3-pip -y
ADD principale.py principale.py
ADD armstrg.py armstrg.py
CMD python3 principale.py