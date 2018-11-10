# Installation

This installation has been tested on **Ubuntu 16.04 LTS** with **Python 3.6 and 3.7** using Anaconda.



## Create Conda Environment

If you don't have Anaconda, please install it following [this guide](https://conda.io/docs/user-guide/install/linux.html).

Then, you can create `sf3` environment using the `environment.yml` provided in this repository.

```
conda env create -f environment.yml
```

You should get logs something like this:

```
Solving environment: done

Downloading and Extracting Packages
openssl-1.0.2p       |  3.5 MB | ########################################################################################################################################## | 100%
libxml2-2.9.8        |  2.0 MB | ########################################################################################################################################## | 100%
pcre-8.42            |  251 KB | ########################################################################################################################################## | 100%
expat-2.2.6          |  187 KB | ########################################################################################################################################## | 100%
gstreamer-1.14.0     |  3.8 MB | ########################################################################################################################################## | 100%
fontconfig-2.13.0    |  291 KB | ########################################################################################################################################## | 100%
freetype-2.9.1       |  822 KB | ########################################################################################################################################## | 100%
certifi-2018.10.15   |  138 KB | ########################################################################################################################################## | 100%
libxcb-1.13          |  502 KB | ########################################################################################################################################## | 100%
ca-certificates-2018 |  124 KB | ########################################################################################################################################## | 100%
libuuid-1.0.3        |   16 KB | ########################################################################################################################################## | 100%
glib-2.56.2          |  5.0 MB | ########################################################################################################################################## | 100%
qt-5.9.6             | 87.1 MB | ########################################################################################################################################## | 100%
python-3.7.0         | 30.6 MB | ########################################################################################################################################## | 100%
gst-plugins-base-1.1 |  6.3 MB | ########################################################################################################################################## | 100%
libpng-1.6.35        |  335 KB | ########################################################################################################################################## | 100%
dbus-1.13.2          |  554 KB | ########################################################################################################################################## | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Collecting numpy (from -r /home/rlee/git/rl-streetfighter/condaenv.ts3voll6.requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/38/39/f73e104d44f19a6203e786d5204532e214443ea2954917b27f3229e7639b/numpy-1.15.4-cp37-cp37m-manylinux1_x86_64.whl (13.8MB)
    100% |████████████████████████████████| 13.9MB 2.8MB/s
Installing collected packages: numpy
Successfully installed numpy-1.15.4
Collecting MAMEToolkit (from -r /home/rlee/git/rl-streetfighter/condaenv.ts3voll6.requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/e9/ad/39864cd62b6aa1ef9bfcf53df21c8922ffab7f353fdde6daefcf6a69816a/MAMEToolkit-1.0.2-py3-none-any.whl (60.3MB)
    100% |████████████████████████████████| 60.3MB 670kB/s
Installing collected packages: MAMEToolkit
Successfully installed MAMEToolkit-1.0.2
#
# To activate this environment, use
#
#     $ conda activate sf3
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Activate the `sf3` environment with one of the following commands below.

```
conda activate sf3
source activate sf3
```

## MAME

There are [quite a few prerequisite Ubuntu packages](https://docs.mamedev.org/initialsetup/compilingmame.html#debian-and-ubuntu-including-raspberry-pi-and-odroid-devices) for MAME.

```
sudo apt-get install git build-essential libsdl2-dev libsdl2-ttf-dev libfontconfig-dev qt5-default
```

We also need to update `libstdc++6`. Since it is not in default repositories, we also need to add a repository. [[Source]](https://github.com/tensorflow/serving/issues/819#issuecomment-374526534)

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get upgrade libstdc++6
```



## Qt

Creating a conda environment with `environment.yml` should have installed Qt on your computer. Verify this with the `qmake` command:

```
qmake -version
```

```
QMake version 3.1
Using Qt version 5.9.6 in /home/rlee/anaconda3/sf3/lib
```

Set an environment variable `LD_LIBRARY_PATH` to the same location. (**WARNING: Change `/rlee/` to match your computer!**)

```
export LD_LIBRARY_PATH=/home/rlee/anaconda3/envs/sf3/lib
```



## Download ROM

Download `sfiii3n.zip` from [some ROM website](https://edgeemu.net/details-24413.htm) and put it in `roms/` directory.




## Run Test Script

Try running `test_installation.py`:

```
python test_installation.py
```

A full screen MAME emulator should start, and after about 10 seconds, the emulator should quit. The console logs should be:

```
[test] Loaded SF3 from ROM file
[test] Wait until learnable gameplay starts...
[test] Start!
[test] Your installation is complete!
```

**If you have trouble installing, check the [TroubleShotting](TROUBLESHOOTING.md) document.**
