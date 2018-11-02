# Lesson 6 (week 6) for PYTHON210B, Autumn 2018 (November 7, 2018)

## Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Online/remote class today using [Zoom](https://washington.zoom.us/my/python2018)
* Due dates for week 6
  * Lesson 6 Assignment by 11:59pm, Tuesday, Nov. 13, 2018 (15 points, Canvas submission of your source files required, one GitHub PR for the assignment required)
    * Mailroom, Part 4: https://canvas.uw.edu/courses/1231462/modules/items/8759013
  * No-submission/grade labs:
    * [Unit testing lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/unit_testing.html)
    * [Args and kwargs lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs_lab.html)

## Modules and Packages

* More examples in [`examples/modules`](../examples/modules) and [`examples/packaging`](../examples/packaing)
  * Do `git pull upstream master` and browse source files in the `examples/*` directory
  * Go over a practical example in [`examples/packaging/capitalize`](../examples/packaging/capitalize)
    * There's also a good pytest example at [`test_capital_mod.py`](../examples/packaging/capitalize/test_capital_mod.py)

## Unit testing

* Go over [the whole page](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Testing.html)
  * `pip install pytest` (or `pip3 install pytest` on Linux or Mac) before trying pytest
  * The `IntroPython-2017\Examples\Session06` directory should be read as [`examples/testing`](../examples/testing)
  * TDD with `cigar_party.py` and `test_cigar_party.py`
* Go over code examples in [`examples/testing`](../examples/testing)
* [Unit testing in VS Code](https://code.visualstudio.com/docs/python/unit-testing)
  * Will need to enable some settings. Can be figured out on the fly.
  * Don't rely on it too much yet (because our git repo has many projects in it, which may not work well with unit test frameworks)

## Advanced argument passing

* Go over [the whole page](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/AdvancedArgumentPassing.html)
  * Keyword arguments and defaults
    * **Important** Defaults are evaluated only once when the function is **defined**, not whenever it's called.
  * Positional args are a tuple, keyword args are a dict
    * Positional args always first, keyword args follow
    * Can pass a tuple as positional args
    * Can pass a dict as keyword args: We've already done this once in dict_lab. Also explained [here](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/AdvancedArgumentPassing.html#passing-a-dict-to-str-format)
  * Keyword-only args: [here](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/AdvancedArgumentPassing.html#keyword-only-arguments)
  * Probably too much flexibility that's confusing to beginners... (like many others in Python)

## More on mutability

* Go over [the whole page](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MoreOnMutability.html) if time permits
  * Shallow copy vs deep copy: [The copy module](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MoreOnMutability.html#the-copy-module)
  * [Mutables as default arguments](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MoreOnMutability.html#mutables-as-default-arguments)
    * Note that function argument defaults are evaluated when the function is **defined** (only once), not every time it's called.
