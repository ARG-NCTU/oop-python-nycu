FROM osrf/ros:noetic-desktop-full

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO noetic

ENV SHELL=/bin/bash \
    USER=rsa \
    UID=1000

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 
    
ENV HOME=/home/${USER}

WORKDIR /home/${USER}

RUN cp /root/.bashrc ~/.bashrc

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
        locales \
        curl \
        cmake \
        make \
        git \
        vim \
        wget \
        sudo \
        lsb-release \
        build-essential \
        net-tools \
        apt-utils \
        software-properties-common \
        dialog \
        libffi-dev \
        python3-dev \
        python3-pip \
        python3-setuptools \
        apt-transport-https \
        libglew-dev \
        python3-tk

RUN pip3 install --upgrade pip \
    && pip3 install --upgrade setuptools \
    && pip3 install \
        python_tsp \
        pypozyx \
        pytest \
        scipy \
        opencv-python \
        dbg \
        pytransform3d \
        pandas


RUN apt-get install less
RUN pip3 install pytest-profiling
RUN apt install python3-ipdb -y
################################# sklearn #####################################
RUN pip3 install scikit-learn
################################# tkinter #####################################
RUN apt-get install -y python3-tk

RUN pip3 install mypy
################################# mkdocs #####################################
RUN pip3 install mkdocs
RUN pip3 install mkdocs-with-pdf
RUN pip3 install mkdocstrings
RUN pip3 install mkdocs-material
RUN pip3 install mkdocstrings[python]
################################# mkdocs-mermaid2-plugin ################################
RUN cd ${HOME} && git clone https://github.com/fralau/mkdocs-mermaid2-plugin.git \
    && cd mkdocs-mermaid2-plugin \
    && python3 setup.py install
################################# networkx[all] #########################################
RUN pip3 install networkx[all]

RUN apt install tree

RUN pip3 install xdoctest 

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
&& apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
ros-${ROS_DISTRO}-rosbridge-server


RUN echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc
