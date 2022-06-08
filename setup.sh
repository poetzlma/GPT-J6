wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

conda create -n GPT-J6 python=3.9

conda activate GPT-J6

# check cuda version
nvcc --version

conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia -y

pip install transformer