FROM ubuntu

RUN apt-get update
RUN apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev -y
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
RUN apt-get install libxvidcore-dev libx264-dev -y
RUN apt-get install libgtk-3-dev -y
RUN apt-get install libatlas-base-dev gfortran libgtk2.0-0 libsm6 python-opencv -y
RUN apt-get install python -y
RUN apt-get install python-pip -y

RUN pip install numpy

WORKDIR /usr/src/app
COPY . .

CMD ["python", "./recognize-face.py"]
