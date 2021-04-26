FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
        libopencv-dev \
        python3-pip \
        python3-opencv \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
        tensorflow \
        numpy \
        pandas \
        sklearn \
        matplotlib \
        seaborn \
        jupyter \
        pyyaml \
        h5py \
        requests \
    && pip3 install keras --no-deps \
    && pip3 install opencv-python imutils \
    && mkdir /app

COPY ./* /app/

CMD ["python3", "/app/main.py"]
