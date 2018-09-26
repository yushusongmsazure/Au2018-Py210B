# Orientation for PYTHON210B, Autumn 2018 (September 26, 2018)

## Topics

### Set up Python programming environment: Python, modules, git

* [Windows](https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/python_for_windows.html)
  * Python 3.7 (64-bit recommended): [link](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)
    * Pay attention to the installation location and other options...
  * [gitbash](https://git-for-windows.github.io/)
    * Git editor choice might be interesting (have never done this myself)
    * Also the CR-LF conversion setting...
    * Also the python alias (to cope with the hanging command line execution)
  * pip, ipython (modules): Follow the python commands in the page
  * I'd like all this to be demoed over Zoom, so a volunteer is requested!
* [Mac](https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/python_for_mac.html)
  * Need some help from a Mac owner!
* [Linux](https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/python_for_linux.html)
  * Does anyone use Linux as desktop/GUI-purpose (not a cynic/sarcastic question, but I'm serious)

### Optional: Editor

* Sublime or Atom: [link](https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/dev_environment/index.html#minimum-requirements)
  * Not endorsed or supported officially, but we are here to help/support in collaboration.
* Visual Studio Code: [link](https://code.visualstudio.com/)
  * Need a little more (extensions) for Python: [link](https://code.visualstudio.com/docs/languages/python)
  * Again, not officially endorsed or supported, but I myself (instructor) will use this throughout the course.
  * I'd say it's an editor (light-weight), which is almost like an IDE (features), so I personally use this most of the time.
  * Settings:
    * Render whitespace to All
    * Shell:Windows to bash path
* (Really optional) Github class repo forking and making the first commit/PR
  1. First, create your github account (if you haven't) at [github](https://github.com/)
  1. Fork our [class repo](https://github.com/UWPCE-PythonCert-ClassRepos/Au2018-Py210B) into your github account
  1. Clone your forked repo to your local workstation (your forked repo becomes the `origin` remote on your local git repo)
  1. Add the github class repo as a remote on your local repo (the `upstream` remote)
  1. Pull from `upstream` (nothing for the first time, but something thereafter)
  1. Push to `origin` (to sync your forked repo with the class repo)
  1. Make your own student subdirectory under the `students` directory
  1. Create your own `README.md` file that says anything (about you, about anything)
  1. Add your new file to your local repo, commit it
  1. Push your commit to your github repo (the `origin` remote)
  1. (For future: Repeat the above 3 steps as frequently as possible as needed)
  1. Create a PR (Pull Request) against the upstream (our class repo)
  1. Wait for your PR to get approved/merged
  1. Add the class repo to your local repo as a remote (name it `upstream`)
  1. Pull from `upstream`
  1. Push to `origin`
  1. Repeat the cycle (go back and repeat from 'Pull from `upstream`' step)
