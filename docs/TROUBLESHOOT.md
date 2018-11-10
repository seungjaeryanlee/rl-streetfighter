# Troubleshooting

## Possible Errors

In a perfect world, the setup should now be completed. However, when you try running `test_installation.py`, you might get these errors.



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

The command returns the Qt version and the installation location.

```
QMake version 3.1
Using Qt version 5.9.6 in /home/rlee/anaconda3/sf3/lib
```

If you get different version, install `qt` with conda.

```
conda install qt
```

Otherwise, copy the installation location to the environment variable `LD_LIBRARY_PATH`.

```
export LD_LIBRARY_PATH=/home/rlee/anaconda3/envs/sf3/lib
```

**If you have still have trouble installing, please leave an issue on [this GitHub repo](https://github.com/seungjaeryanlee/rl-streetfighter).**
