FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
    
ENV ROS_DISTRO=noetic \
    SHELL=/bin/bash \
    NB_USER=arg \
    NB_UID=1000

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


################################## Python3.8 #####################################
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-dev \
    python3.8-tk \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN python3.8 -m pip install --upgrade pip setuptools wheel && \
    mkdir -p /home/${NB_USER}/.local/lib/python3.8/site-packages && \
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
    vulkan-utils \
    mesa-vulkan-drivers \
    pigz \
    git \
    libegl1 \
    git-lfs \
    xvfb \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Force gcc 9 to avoid CUDA 10 build issues on newer base OS
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100

################################## python tools #####################################
RUN python3.8 -m pip install \
    numpy \
    matplotlib \
    pandas \
    gdown \
    pyautogui \
    pytest \
    Pillow \
    tensorboard \
    tensorflow \
    swig \
    warp-lang \
    urdfpy \
    networkx

################################## torch gymnasium sb3 #####################################
RUN python3.8 -m pip install --no-cache-dir --ignore-installed PyYAML \
    && python3.8 -m pip install \
    torch \
    torchaudio \
    torchvision \
    gymnasium \
    gymnasium[box2d] \
    stable-baselines3 \
    openai==0.27.0 \
    trajectopy-core \
    huggingface-sb3 \
    huggingface_hub \
    transformers \
    datasets \
    hf_transfer \
    opencv-python-headless \
    timm

################################## IsaacGym #####################################
# Download Isaac Gym from NVIDIA and extract it
RUN wget https://developer.nvidia.com/isaac-gym-preview-4 -O /tmp/IsaacGym_Preview_4_Package.tar.gz && \
    tar -xvzf /tmp/IsaacGym_Preview_4_Package.tar.gz -C /opt && \
    rm /tmp/IsaacGym_Preview_4_Package.tar.gz && \
    cd /opt/isaacgym && \
    git clone https://github.com/isaac-sim/IsaacGymEnvs.git && \
    chown -R ${NB_USER}:${NB_GID} /opt/isaacgym && \
    chown -R ${NB_USER}:${NB_GID} /opt/isaacgym/IsaacGymEnvs

# Change ownership of the Isaac Gym directory to the non-root user
# RUN chown -R ${NB_USER}:${NB_GID} /opt/isaacgym \
#     && chown -R ${NB_USER}:${NB_GID} /opt/IsaacGymEnvs

# Switch to the non-root user
USER ${NB_USER}

# Install gym modules
ENV PATH="${HOME}/.local/bin:$PATH"
RUN pip3 install -q -e /opt/isaacgym/python && \
    pip3 install -q -e /opt/isaacgym/IsaacGymEnvs
ENV NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=all \
    VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
USER root
# RUN pip3 install git+https://github.com/isaac-sim/IsaacGymEnvs.git
################################## aerial_gym_simulator #########################
RUN pip3 install git+https://github.com/mmatl/urdfpy.git
# Switch to the non-root user
WORKDIR /opt
RUN git clone https://github.com/ntnu-arl/aerial_gym_simulator.git && \
    cd aerial_gym_simulator && \
    pip3 install -q -e .


RUN echo "root ALL=(ALL)  ALL" >> /etc/sudoers \
    && echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc 

ENV XLA_PYTHON_CLIENT_PREALLOCATE=false
ENV HF_HUB_ENABLE_HF_TRANSFER=1