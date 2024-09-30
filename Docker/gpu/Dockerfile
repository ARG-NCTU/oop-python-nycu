FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

###################################### user #####################################

ENV SHELL=/bin/bash \
    USER=arg \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

###################################### basic tools #####################################

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \ 
    locales \
    cmake \
    unzip \
    make \
    git \
    vim \
    gedit \
    wget \
    sudo \
    lsb-release \
    build-essential \
    net-tools \
    dirmngr \
    gnupg2 \
    mercurial \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libpcap-dev \
    python3-pip \
    python3-setuptools \
    python3-opencv \
    python3-numpy \
    python3-empy  \
    python3-dev \ 
    python3-tk \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

##################################### PIP ######################################

RUN pip3 install --upgrade pip setuptools

RUN pip3 install ale-py==0.8 \
    orjson \
    gymnasium \
    gymnasium[atari] \
    gymnasium[accept-rom-license] 

RUN pip3 install \
    matplotlib \
    pandas \
    torch \
    torchaudio \
    torchvision \
    quart \
    rich \
    opencv-python
    
RUN pip3 install stable-baselines3[extra]

RUN pip3 install scikit-learn

RUN pip3 install swig
RUN pip3 install gymnasium[box2d]

################################# tkinter #####################################
RUN pip3 install mypy

##################################### HuggingFace #####################################
RUN pip3 install transformers \
    datasets \
    evaluate \
    transformers[sentencepiece] \
    accelerate \
    timm \
    albumentations
##################################### Roma #####################################
RUN pip3 install roma
RUN pip3 install jupyter 
RUN pip3 install ipytest

##################################### Sound effect #####################################
RUN pip3 install soundfile librosa jiwer transformers[torch]

RUN pip3 install cupy-cuda111

##################################### CMake 3.30.0 #####################################
RUN wget https://cmake.org/files/v3.30/cmake-3.30.0-linux-x86_64.sh
RUN chmod +x cmake-3.30.0-linux-x86_64.sh
RUN bash cmake-3.30.0-linux-x86_64.sh --skip-license --prefix=/usr/local

##################################### setting ###################################################

RUN chown -R ${USER}:${USER} ${HOME}/
RUN echo "${USER} ALL=(ALL)  ALL" >> /etc/sudoers

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all

USER ${USER}
WORKDIR ${HOME}
CMD ["/bin/bash"]