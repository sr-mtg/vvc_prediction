sudo apt update && sudo apt upgrade
#install ffmpeg
sudo apt -y install ffmpeg
ffmpeg -version
#install git
sudo apt -y install ffmpeg
#install nasm
sudo apt-get -y install nasm
#install cmake
sudo apt -y install cmake g++ make
#insatll VCA
git clone https://github.com/cd-athena/VCA.git
cd VCA/
mkdir build
cd build/
cmake ../
cmake --build .