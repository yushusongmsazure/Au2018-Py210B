# Lesson 1 (week 1) for PYTHON210B, Autumn 2018 (October 3, 2018)

## Topics

### Logistics

* Attendance check: https://canvas.uw.edu/courses/1231462/external_tools/8851
  * 80% attendance required to pass the course
* Course Canvas site access: https://canvas.uw.edu/courses/1231462
  * Everyone must have access to the site. Let me know if anyone doesn't.
* Course email list: https://piazza.com/class/jma0wi35h6sfu
  * Everyone must have received an invite and joined the list. Let me know if anyone hasn't.
  * Make sure your UWNetID is active and configured to receive email!
* Assignments due Friday, 10/5/2018
  * Lesson 1 Exercise (3 points): https://canvas.uw.edu/courses/1231462/modules/items/8758981
  * Lesson 1 Activity (ungraded): https://canvas.uw.edu/courses/1231462/modules/items/8758983

### Git & Github concepts

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Git.html

### Github class repo forking and making the first commit/PR

1. First, create your github account (if you haven't) at [github](https://github.com/)
    * Note everything on your github account is public, so decide whether to use your real name or an alias (which is fine--just let us know in private).
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
1. Create a PR (Pull Request) against the upstream (our class repo) if you'd like your code to be reviewed by instructors, or if a PR is required as an activity/assignment (for potential peer code review)
1. Wait for comments in your PR, for it to get approved/merged, or proceed if it's delayed (pinging the instructors is OK for PR review request)
1. Repeat the cycle (go back and repeat from 'Pull from `upstream`' step)

### Basic Python

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/BasicPython.html
* Use iPython for REPL (Python still works, but iPython is better for interactive sessions)
* Try running Python script files provided in `examples/tutorial` directory
  * Either on your shell (bash) or on iPython (start using iPython commands like `cd` to navigate the directory hierarchy within iPython)
* Create a Python script file, run it on iPython or from your shell (using `python my_first_python_script.py`)
  * May configure VSCode for gitbash terminal (Windows)
* Now ready to start and complete the Lesson 1 Activity assignment
  * https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/python_pushups.html
  * Use your git local repo and follow the instructions exactly
  * Submit your `*.py` files to the Canvas assignment submission page for grading purposes
  * Also submit a github PR for peer review and/or for assistance from instructors
    * If you have any questions while you are coding, you can submit a github PR with your current code and email us for help
    * Or other students can help by providing their own PR feedback--collaborative learning
    * Just make sure that you don't copy someone else's code from their PRs or check-ins.
