# 설치

이 설치법은 **Ubuntu 16.04 LTS** 에서 **Anaconda**와 **Python 3.6, 3.7** 사용했을 때 정상작동하는 것을 확인했습니다.



## Conda Environment 만들기

컴퓨터에 Anaconda 가 없다면 , [이 가이드](https://conda.io/docs/user-guide/install/linux.html)를 따라 설치하세요.

그 후, 아래의 커맨드로 이 레포지토리에 있는 `environment.yml`을 통해 `sf3` 라는 이름의 환경을 만드세요.

```
conda env create -f environment.yml
```

`sf3` 환경을 만들 때, 아래와 같은 로그가 출력될 것입니다.

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

아래의 커맨드 중 하나를 써서 `sf3` 환경을 활성화시키세요.

```
conda activate sf3
source activate sf3
```

## MAME

MAME를 컴파일하기 위해서는 [여러 개의 우분투 패키지](https://docs.mamedev.org/initialsetup/compilingmame.html#debian-and-ubuntu-including-raspberry-pi-and-odroid-devices) 가 필요합니다. 아래 커맨드로 설치하세요.

```
sudo apt-get install git build-essential libsdl2-dev libsdl2-ttf-dev libfontconfig-dev qt5-default
```

또 `libstdc++6` 라는 우분투 패키지를 업데이트해야 하는데. 이 패키지의 최신버전이 기본 레포지토리에 없으므로, 레포지토리를 추가한 후 업그레이드해야 합니다. [[출처]](https://github.com/tensorflow/serving/issues/819#issuecomment-374526534)

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get upgrade libstdc++6
```



## Qt

`environment.yml` 을 사용해서 `sf3` 환경을 만들었다면, 컴퓨터에 Qt가 설치되었을 것입니다. `qmake` 커맨드로 그런지 확인하세요.

```
qmake -version
```

아래와 같이 5.9 버전과 라이브러리 경로가 출력되었다면 정상입니다.

```
QMake version 3.1
Using Qt version 5.9.6 in /home/rlee/anaconda3/sf3/lib
```

`LD_LIBRARY_PATH`라는 환경 변수를 이 라이브러리 경로가 되게 세팅합니다.


```
export LD_LIBRARY_PATH=/home/rlee/anaconda3/envs/sf3/lib
```

**참고: 환경변수를 세팅하는 위 커맨드는 현재 터미널에만 적용됩니다. 즉, 새로운 터미널에서 플레이하려면 저 커맨드를 다시 써야 합니다.**



## ROM 다운로드

[적당한 ROM 웹사이트](https://edgeemu.net/details-24413.htm)에서 `sfiii3n.zip` ROM 파일을 다운받아서 `roms/`에 넣으세요.




## 설치 테스트하기

`test_installation.py` 스크립트를 실행시키세요:

```
python test_installation.py
```

전체화면으로 SF3가 로드된 MAME 에뮬레이터가 시작하고, 약 10초 후에 꺼질 것입니다. 정상적으로 설치되었다면 출력은 아래와 같을 것입니다.

```
[test] Loaded SF3 from ROM file
[test] Wait until learnable gameplay starts...
[test] Start!
[test] Your installation is complete!
```

**If you have trouble installing, check the [TroubleShooting](TROUBLESHOOT.md) document.**
