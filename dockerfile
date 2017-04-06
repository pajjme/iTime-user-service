FROM python:3.6.1-onbuild
COPY . /usr/src/app
CMD ["python","-u","main.py"]
