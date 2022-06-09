sudo apt update
sudo apt upgrade



# get nvidia driver

sudo add-apt-repository ppa:graphics-drivers
sudo apt update
# to check for driver version needed see
# ubuntu-drivers devices
sudo apt install nvidia-driver-515

sudo reboot

nvidia-smi

sudo reboot


# get cuda

sudo wget -O /etc/apt/preferences.d/cuda-repository-pin-600 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"

sudo apt update
sudo apt install cuda

echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc

nvcc --version

# 

sudo apt install python3-pip
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113