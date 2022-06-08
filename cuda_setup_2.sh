#!/bin/bash
## This gist contains instructions about cuda v11.1 and cudnn 7.6 installation in Ubuntu 20.04 for Tensorflow 2.1.0

### steps ####
# verify the system has a cuda-capable gpu
# download and install the nvidia cuda toolkit and cudnn
# setup environmental variables
# verify the installation
###

### If you have previous installation remove it first. 
sudo apt-get purge nvidia*
sudo apt remove nvidia-*
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt-get autoremove && sudo apt-get autoclean
sudo rm -rf /usr/local/cuda*


### to verify your gpu is cuda enable check
lspci | grep -i nvidia

### gcc compiler is required for development using the cuda toolkit. to verify the version of gcc install enter
gcc --version

# system update
sudo apt-get update
sudo apt-get upgrade


# install other important packages
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev


# first get the PPA repository driver
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list
sudo apt-get update

 # installing CUDA-11.1
sudo apt-get -o Dpkg::Options::="--force-overwrite" install cuda-11-1 cuda-drivers


# setup paths
echo 'export PATH=/usr/local/cuda-11.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

# in order to download cuDNN you have to be registered here https://developer.nvidia.com/developer-program/signup
# then download cuDNN for 11.1 from https://developer.nvidia.com/cudnn

# u can copy it to folder in vscode

#i am not sure
CUDNN_TAR_FILE="cudnn-linux-x86_64-8.4.1.50_cuda11.6-archive.tar.xz"
tar -xf ${CUDNN_TAR_FILE}

# copy the following files into the cuda toolkit directory.
sudo cp -P cudnn-linux-x86_64-8.4.1.50_cuda11.6-archive/include/cudnn.h /usr/local/cuda-11.1/include
sudo cp -P cudnn-linux-x86_64-8.4.1.50_cuda11.6-archive/lib/libcudnn* /usr/local/cuda-11.1/lib64/
sudo chmod a+r /usr/local/cuda-11.1/lib64/libcudnn*

# Finally, to verify the installation, check
nvidia-smi
nvcc -V

# install Tensorflow (an open source machine learning framework)
# I choose version 2.1.0 because it is stable and compatible with CUDA 10.1 Toolkit and cuDNN 7.6

sudo pip3 install --user tensorflow-gpu==2.1.0