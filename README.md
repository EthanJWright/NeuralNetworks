### Convolutional Neural Networks

#### Neural Network Environment
The guide for getting the environment setup was adapted from [here](https://www.pyimagesearch.com/2017/09/25/configuring-ubuntu-for-deep-learning-with-python/)

1. Install Ubuntu Dependencies
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake git unzip pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libhdf5-serial-dev graphviz
sudo apt-get install libopenblas-dev libatlas-base-dev gfortran
sudo apt-get install python-tk python3-tk python-imaging-tk
sudo apt-get install python2.7-dev python3-dev
```

2. Setup Virtal Environment
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip get-pip.py
```
3. Add Virtual Environment Things to bashrc
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

4. Start Virtual Environment
```
source ~/.bashrc
mkvirtualenv cnn -p python3
workon cnn
```

5. Install Python ML Requirements
```
sudo -H pip install numpy
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
cd ~/opencv-3.3.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D WITH_CUDA=OFF \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
  -D BUILD_EXAMPLES=ON ..

make -j4

sudo make install
sudo ldconfig
cd ~
rm -rf opencv-3.3.0 opencv.zip
rm -rf opencv_contrib-3.3.0 opencv_contrib.zip
```

6. Configure Ubuntu for Python DL
```
cd ~/.virtualenvs/dl4cv/lib/python3.6/site-packages/
ln -s /usr/local/lib/python3.6/site-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so
cd ~
```

7. Install Keras
```
pip install scipy matplotlib pillow
pip install imutils h5py requests progressbar2
pip install scikit-learn scikit-image
pip install tensorflow
pip install keras
```

#### Navigate to sub directories for tutorials on specific code. ( vggnet recommended)
