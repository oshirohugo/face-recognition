# Face Recognition

## Before using the scripts

You should have python 2 installed in your system and some python libraries: opencv-python 2.x and numpy.
If you don't have this environment you can use docker as explained on [Build and running inside docker](#build-and-running-inside-docker) to run the scripts. Or a dev image as explained [here](https://github.com/oshirohugo/opencv-python-dev-dockerfile)

## Using the scripts

The face recognition only works with after face recognizer is generated.

To generate a face reconizer first you have to create a data set:

```bash
$ ./create-dataset.py $USER_ID data-set
```

To train the face recognizer

```bash
$ ./train.py data-set trainner
```

After that you can run the face reconition script

```bash
$ ./recognize-face.py
```

It needs that the reconizer file is located on `trainner/trainner.yml`

## Build and running inside docker
If you don't want to set an environmet to run the scripts, you can use the provided `Dockerfile` to build and image and run the container:

```bash
$ docker build . -t <image-name>
```

To run it you have to adjust the permission to the X server host. So run the following command in the docker host machine:

```bash
$ xhost +local:root
```

This is a lazy workaround to permit connection from the container, and it can be improved as explained [here](http://wiki.ros.org/docker/Tutorials/GUI).

After that you can run your docker container:

```bash
$ docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device /dev/video0 \
    <image-name>
```

or just use the provided script:

```bash
$ ./run-dev-container.sh <image-name>
```

when you finish, disable permission to connect to your X server host:

```bash
$ xhost -local:root
```
