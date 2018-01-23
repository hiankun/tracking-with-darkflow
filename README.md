# Introduction

* This repository (including the submodules) was manually copied from [bendidi/Tracking-with-darkflow](https://github.com/bendidi/Tracking-with-darkflow).
  * The original `README.md` has been moved to `README_orig.md`
  * Copy date: 2017/12/19

* I tried this repository in Ubuntu 16.04 within a conda environment (FYI: `repo/conda_env.yml`).

# For Anaconda 3 Users

## The OpenCV Problems

* AFAIK, the OpenCV versions from `conda` or `pip` has no complete video functions, so you'll encounter problems when running the code which calls video reading or writing functions.

* Make sure to install OpenCV manually before installing Anaconda.
  * I had tried to build OpenCV when my system already has Anaconda 3 installed, and it never worked.
  * This step is just a workaround. If you know better approaches, welcome to leave me a message.

* After build and install OpenCV in your system, do the following things to install Anaconda and make it access to your system's OpenCV:
  * install Anaconda 3
  * create a test environment by `conda create -n <your_env_name> python=3.6` (or use `repo/conda_environment.yml`)
  * go to `~/.conda/envs/<your_env_name>/lib/python3.6/site-packages`
  * link the so file by

    `ln -s /usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so`

  * to check whether it works, you could go to `repo` and run `python check_vid_play.py <test_video_file>`.

# Usage (in your conda environment)
* Download the repository, go to `darkflow` folder, then run `python3 setup.py build_ext --inplace`.
* Edit the `run.py` to fit your mission.
* Run `python run.py` and watch the results. :-)
