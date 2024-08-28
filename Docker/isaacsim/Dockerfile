FROM nvcr.io/nvidia/isaac-sim:4.0.0

ARG DEBIAN_FRONTEND=noninteractive
    
ENV ROS_DISTRO=noetic \
    SHELL=/bin/bash \
    NB_USER=arg \
    NB_UID=1001

RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime

###################################### user #####################################
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER} 

RUN echo "root:root" | chpasswd \
    && echo "${NB_USER}:111111" | chpasswd

ENV HOME=/home/${NB_USER}


################################## python3.10 #####################################
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3.10-tk \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN python3.10 -m pip install --upgrade pip setuptools wheel && \
    mkdir -p /home/${NB_USER}/.local/lib/python3.10/site-packages && \
    mkdir -p /home/${NB_USER}/.cache/pip && \
    chown -R ${NB_USER}:${NB_GID} /home/${NB_USER}/.local && \
    chown -R ${NB_USER}:${NB_GID} /home/${NB_USER}/.cache/pip

################################## Basic tools #####################################
RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade && \
    apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    curl \
    vim \
    wget \
    sudo \
    cmake \
    gedit \
    gnupg2 \
    gtk+-3.0 \
    locales \
    dirmngr \
    mercurial \
    net-tools \
    lsb-release \
    openssh-client \
    build-essential \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libpcap-dev \
    libusb-1.0 \
    tzdata \
    libglfw3-dev \
    libmetis-dev \
    software-properties-common \
    ruby libfltk1.3-dev \
    freeglut3-dev \
    libpng-dev \
    libjpeg-dev \
    libxft-dev \
    libxinerama-dev \
    libtiff5-dev \
    librapidxml-dev \
    netbase \
    fluid \
    xterm \
    scrot \
    g++ \
    subversion \
    libtiff-dev \
    espeak \
    qtbase5-dev \
    ifstat \
    iperf3 \
    libxcursor-dev \
    libxrandr-dev \
    libxi-dev \
    mesa-common-dev \
    zip \
    unzip \
    make \
    gcc-9 \
    g++-9 \
    mesa-vulkan-drivers \
    pigz \
    git \
    libegl1 \
    git-lfs \
    xvfb \
    ffmpeg \
    x11-xserver-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Force gcc 9 to avoid CUDA 10 build issues on newer base OS
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100

################################## python tools #####################################
RUN python3.10 -m pip install \
    numpy \
    matplotlib \
    pandas \
    gdown \
    pyautogui \
    pytest \
    Pillow \
    tensorboard \
    swig \
    warp-lang \
    urdfpy \
    networkx

################################## torch gymnasium sb3 #####################################
RUN python3.10 -m pip install --no-cache-dir --ignore-installed PyYAML \
    && python3.10 -m pip install \
    torch \
    torchaudio \
    torchvision \
    gymnasium \
    gymnasium[box2d] \
    stable-baselines3 \
    openai \
    trajectopy-core \
    huggingface-sb3 \
    huggingface_hub \
    transformers \
    datasets \
    hf_transfer \
    opencv-python-headless \
    timm

################################## IsaacSim #####################################
RUN python3.10 -m pip install \
    isaacsim==4.1.0.0 --extra-index-url https://pypi.nvidia.com \
    isaacsim-extscache-physics==4.1.0.0 isaacsim-extscache-kit==4.1.0.0 isaacsim-extscache-kit-sdk==4.1.0.0 --extra-index-url https://pypi.nvidia.com


RUN echo "root ALL=(ALL)  ALL" >> /etc/sudoers 
    # && echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc 


ENV XLA_PYTHON_CLIENT_PREALLOCATE=false \
    HF_HUB_ENABLE_HF_TRANSFER=1 \
    OMNI_KIT_ACCEPT_EULA=YES \