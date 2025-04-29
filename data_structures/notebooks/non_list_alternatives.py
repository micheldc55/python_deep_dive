

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import random
    from time import perf_counter

    import marimo as mo
    import numpy as np
    return mo, np, perf_counter, random


@app.cell
def _(mo):
    mo.md(
        r"""
        # Non-list Alternatives

        Did you know that there is an array-type in Python similar to Numpy's `np.ndarray` ? Did you know that if you need to access or prepend/append elements only to the beginning or end of a sequence there are list alternatives optimized for it?

        I sure didn't, so this is my exploration of some of these alternative data structures that I'm not that familiar with.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 1) array.array: the Python native array structure

        Python has a native array implemented in Python's C backend. It works very similarly to the arrays you can create in `C`, which have a data type specified as a letter ('B': bytes, 'd': double/float, 'b': signed char/int). This letter is called the typecode as we'll see below and can also be positionally referenced.

        If you have used Numpy before, you'll know that you need to install Numpy from an external source (like PyPi) inside your current Python environment in order to access it. But it turns out Python has a way to implement this arrays natively with the `array.array` library.
        """
    )
    return


@app.cell
def _():
    from array import array
    return (array,)


@app.cell
def _(array):
    arr1 = array('B', range(5))

    print(arr1)
    return (arr1,)


@app.cell
def _(arr1):
    print(type(arr1))
    print(type(arr1[0]))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Note that Python's native array type has differences with the Numpy standard array handling. For example, the `+` or `*` operators work differently than on Numpy arrays, a comparison is shown below:

        - Numpy arrays perform the element-wise multiplication operation when multiplied by a scalar
        - Numpy arrays perform the element-wise addition opertaion when added to another array.
        """
    )
    return


@app.cell
def _(np):
    np_arr = np.array([0, 1, 2, 3, 4], dtype=np.uint8)
    return (np_arr,)


@app.cell
def _(arr1, np_arr):
    print("Python's built-in array multiplied by `2`:", arr1 * 2)
    print("Numpy's array multiplied by the scalar `2`: \t\t ", np_arr * 2)
    return


@app.cell
def _(arr1, np_arr):
    print("Python's built-in array added to itself:", arr1 + arr1)
    print("Numpys's array added to itself:  \t\t\t\t   ", np_arr + np_arr)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Pythons arrays are extremely efficient as they are implemented in native C, but they are not designed for scientific/vectorized operations like Numpy is, so generally NumPy/SciPy is the better choice but it's good to know Python has it's own version of arrays, and they are especially optimized for low memory head.

        You can write and load these built-in arrays extremely fast using the `.tofile` and `.fromfile` methods. A quick demonstration using the built-in performance counter is shown below:
        """
    )
    return


@app.cell
def _(array, random):
    floats_array = array('d', (random.random() for _ in range(10 ** 7)))

    with open("data_structures/notebooks/files/floats.bin", 'wb') as fp:
        floats_array.tofile(fp)
    return


@app.cell
def _(array, perf_counter):
    read_array = array('d')

    t0 = perf_counter()
    with open("data_structures/notebooks/files/floats.bin", 'rb') as fp2:
        read_array.fromfile(fp2, 10**7)
        t1 = perf_counter()
    print(round(1000 * (t1 - t0), 2), "miliseconds")
    return


@app.cell
def _(mo):
    mo.md(r"""The read time of a 10 million double-precision array from binary is blazing-fast at ~20 miliseconds on my mac. But it will depend on your CPU and it will be the output from the cell above.""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
