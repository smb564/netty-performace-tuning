# Netty Performance Tuning
Scripts for running performance tests and tuning algorithm implementations. This is particularly targeted to use with <a>https://github.com/smb564/adaptive-concurrency-control</a>.


## Installing python packages
The most easiest way to install packages for this is to create a virtual environment inside.

Create a virtual environment using the following command. (If you are not familiar just google "python virtual environments")
(The below will create a virtual environment named venv)
```
python3 -m venv venv
```

Now avtivate the virtual environment using the following command.
```
source venv/bin/activate
```

After activating the environment, you should install the packages you will be using. Following packages are required for this project. (You can use pip to install packages)

```
pip install requests matplotlib sklearn numpy scikit-optimize scipy hyperopt
```

## Automation Scripts

At the time of writing, there were two test automation scripts.

`netty_script_dataset.sh` runs a set of experiments and collects results for different use cases with dynamic, and several fixed thread pool sizes

`netty_script.sh` runs a simple bayesian tuning case. You can improve this to run tuning case against the default case and generate comparison plots using the plots (like in TPC-W case).
