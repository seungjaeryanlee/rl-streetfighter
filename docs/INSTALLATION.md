# Installation

This installation has been tested on **Ubuntu 16.04 LTS** with **Python 3.6** using Anaconda.

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
pip-18.1             | 1.7 MB    | ###################################################################### | 100%
wheel-0.32.2         | 35 KB     | ###################################################################### | 100%
python-3.7.1         | 36.4 MB   | ###################################################################### | 100%
sqlite-3.25.2        | 1.9 MB    | ###################################################################### | 100%
certifi-2018.10.15   | 138 KB    | ###################################################################### | 100%
setuptools-40.5.0    | 615 KB    | ###################################################################### | 100%
openssl-1.1.1        | 5.0 MB    | ###################################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Collecting numpy
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

Activate the `sf3` environment.

## MAME

There are [quite a few prerequisite Ubuntu packages](https://docs.mamedev.org/initialsetup/compilingmame.html#debian-and-ubuntu-including-raspberry-pi-and-odroid-devices) for MAME.

```
sudo apt-get install git build-essential libsdl2-dev libsdl2-ttf-dev libfontconfig-dev qt5-default
```

## Possible Errors

In a perfect world, the setup should now be completed. However, when you try running `test_installation.py`, you will probably get these errors.


### `GLIBCXX`

```
./mame: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by ./mame)
```

We need to update `libstdc++6`. Since it is not in default repositories, we also need to add a repository. [[Source]](https://github.com/tensorflow/serving/issues/819#issuecomment-374526534)

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get upgrade libstdc++6
```

### `Qt_5`

```
./mame: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5.9' not found (required by ./mame)
./mame: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5' not found (required by ./mame)
./mame: /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5: version `Qt_5' not found (required by ./mame)
./mame: /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5: version `Qt_5' not found (required by ./mame)
```

First, verify that you have correct version of Qt (5.9).

```
qmake -version
```

You should get something like this:

```
QMake version 3.1
Using Qt version 5.9.6 in /home/rlee/anaconda3/lib
```

Set environment variable `LD_LIBRARY_PATH` to point to Anaconda.

```
export LD_LIBRARY_PATH=/home/rlee/anaconda3/lib
```
