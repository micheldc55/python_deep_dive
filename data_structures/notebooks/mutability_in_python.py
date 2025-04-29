

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Python Quirks about mutability""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Mutability in Python is not always straightforward. Therefore, it's important to be wary about using and having mutable objects, especially as inputs to functions to avoid undesired behavior.

        One of the most notorious mutable elements in Python are lists, but there are other not so intuitive ones that may also be problematic.

        I will go over some of these below for reference.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 1) Tuple mutability

        One of the most surprising to me was tuple mutability. In Python, tuples work as **immutable memory references**. They are generally treated as immutable objects, but this isn't precisely true.
        """
    )
    return


@app.cell
def _():
    tuple1 = (1, "abc", 42)

    tuple1[0] += 1
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        This **reference immutability** means that any tuple will consist of immutable pointers to objects in memory. But this doesn't mean that one can't change tuples in any way. If we attempt tuple assignation as above, we will get an error as we cannot change the reference of the tuple, as expected.

        But what happens if we create a mutable object and create a tuple that uses that element? Internally, Python will create a list of references in memory to each object we created.

        If we create the tuple as:

        ```python
        tuple1 = ('a', 2, 'c')
        ```

        Python will treat the tuple objects as a set of memory pointers all stored during creation. Every time we try to print the tuple, the string representation of the tuple will then go to each of those memory locations and retrieve the corresponding value.

        Imagine these where stored in memory like this:

        tuple1 = (`<fx012b23>`, `<kd90x0002>`, `<fp55hx9091>`)

        Where for each pointer, when we go to retrieve it's value we will find the value of the object we stored there. So, for example, we can create the following tuple:
        """
    )
    return


@app.cell
def _():
    mutable_obj = [1, 2]

    tuple2 = (1, 'abc', mutable_obj, 42)

    print(tuple2)
    return mutable_obj, tuple2


@app.cell
def _(mutable_obj):
    mutable_obj.append('intruder')
    return


@app.cell
def _(mo):
    mo.md(r"""Try to guess what will happen if we print the `tuple2` object, which hasn't been directly modified above.""")
    return


@app.cell
def _():
    selection_options = [
        "tuple2 doesn't change and you will get an error when printing",
        "tuple2 doesn't change, you will get the same as before, tuples are immutable!",
        "tuple2 changes, the list above will have been appeneded with the `intruder` element"
    ]
    return (selection_options,)


@app.cell
def _(mo, selection_options):
    multiselect = mo.ui.radio(
        options=selection_options,
        label="What will happen when we print tuple2??"
    )

    multiselect
    return (multiselect,)


@app.cell(hide_code=True)
def _(multiselect, selection_options):
    if multiselect.value != selection_options[-1]:
        print("Wrong!")
    else:
        print("Correct!")
    return


@app.cell
def _(tuple2):
    print(tuple2)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        If you are like me and thought that tuples were **immutable**, this feels **wrong**. But on the other hand, knowinb Python does it really feel that wrong? We would expect this type of behavior from a list no questions asked...

        So what is the difference? Is a tuple just a list? Not really, as the tuple references are still immutable, and Python tuples are created and stored as fixed length objects as Python doesn't need to preemptively or dynamically allocate extra memory to account for the possibility of us adding / removing elements.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 2) Mutability in multiplication / concatenation

        Another example that caught me off guard is creating multiple lists with the `"*"` sign. In Python you can concatenate two lists using the sumation sign:

        ```python
        list1 = [1, 2]
        list2 = [3, 4]

        list1 + list2
        ```

        ```python
        >>> [1, 2, 3, 4]
        ```

        You can think of the multiplication sign `"*"` as we think about it as a mathematical operation, that applies the sumation between objects `n` times. So, if we do the following:

        ```python
        [1, 2] * 3
        ```

        It's equivalent to doing:

        ```python
        [1, 2] + [1, 2] + [1, 2]
        ```

        And the output will in both cases be:

        ```python
        [1, 2, 1, 2, 1, 2]
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""So what happens when we do a concatenation over a mutable object? Let's start with using immutables, for example Python's `str` object. I'll create a function to display the board in rows for simplicity, but it's not necessary for what I'm trying to show below.""")
    return


@app.function
def display_tictactoe_board(board: list[list]) -> None:
    assert len(board) == 3, "Board must have 3 elements"
    assert all([len(elem) == 3 for elem in board]), "Board elements must have 3 elements each"
    
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")


@app.cell
def _():
    tictactoe1 = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    tictactoe1[2][1] = 'X'

    display_tictactoe_board(tictactoe1)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        We could also create the tictactoe board from a list comprehension to be more succinct, by creating a list of three elements like these:

        `['_', '_', '_']`
        """
    )
    return


@app.cell
def _():
    tictactoe2 = [['_', '_', '_'] for _ in range(3)]

    display_tictactoe_board(tictactoe2)
    return (tictactoe2,)


@app.cell
def _(tictactoe2):
    tictactoe2[0][2] = 'X'

    display_tictactoe_board(tictactoe2)
    return


@app.cell
def _(mo):
    mo.md(r"""Want to see a cool party trick that will only be fun among engineers? We could try to be even more sneaky and do it in an even shorter fashion like this:""")
    return


@app.cell
def _():
    tictactoe3 = [['_', '_', '_']] * 3

    display_tictactoe_board(tictactoe3)
    return (tictactoe3,)


@app.cell
def _(tictactoe3):
    tictactoe3[0][2] = 'X'

    display_tictactoe_board(tictactoe3)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Me: **WHAT???** 

        No one: Welcome to Python 🙂

        Can you guess what's happening here? Mark the checkbox below for the answer.
        """
    )
    return


@app.cell
def _(mo):
    show_solution_list_mult = mo.ui.checkbox(label="Show solution")

    show_solution_list_mult
    return (show_solution_list_mult,)


@app.cell
def _(show_solution_list_mult):
    if show_solution_list_mult.value == True:
        print(
            "This happens because Python will treat concatenation as repeating the same instance 3 times,", 
            "\nwhereas the list comprehension will reinitialize the object 3 times in our scenario. You can think", 
            "\nabout how we could fall into the same pitfall using a list comprehension, but this is left to the ", 
            "\nreader to test out.")
    else:
        print("Click the checkbox above to show the answer...")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 3) Even weirder: In-place addition

        An even weirder scenario than what we discussed above is the in-place addition of mutable sequences in Python. A very brain-twisting example of this can be found in the book [Fluent Python](no-internet-add-link-later!) by Luciano Ramalho, which I'm using as the basis for this repo.

        When doing in-place addition, we can mess up immutable sequences even further as we will see below. Imagine we do the same as in (1) and create an immutable reference sequence like a `tuple`.
        """
    )
    return


@app.cell
def _():
    tuple3 = (1, 2, ['a', 'b'])
    return (tuple3,)


@app.cell
def _(mo):
    mo.md(
        r"""
        What would happen if we take element [2] of the tuple, the list ['a', 'b'] and used in-place addition to it?

        For reference, if we had a list "l" and performed in-place addition (`+=`) to it, we would get:

        ```python
        l = [1, 2]
        l += [8, 9]
        l
        ```
        ```python
        >>> [1, 2, 8, 9]
        ```
        """
    )
    return


@app.cell
def _():
    l = [1, 2]
    l += [8, 9]

    print(l)
    return


@app.cell
def _(mo):
    mo.md(r"""What do you think would happen if we did the same with a list reference assigned to a tuple? Run the cells below and see for yourself... Try guessing first, running the `tuple3[2] += ...` first and then try to guess what will be the value of the tuple3 print as well.""")
    return


@app.cell
def _(tuple3):
    tuple3[2] += ['y', 'z']
    return


@app.cell
def _(tuple3):
    print(tuple3)
    return


@app.cell
def _(mo):
    mo.md(r"""Mind boggling right? Let's try to see what happens in bytecode when we perform in-place addition to a mutable sequence in element [a]. We will use Python's built-in dissassembler library, which dissassembles Python byte-code into a set of mnemonics of somewhat-readable operations.""")
    return


@app.cell
def _():
    import dis

    dis.dis('s[a] += b')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
