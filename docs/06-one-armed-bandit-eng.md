# One-armed bandit but with lists and loops {#One-armed-bandit}

In this chapter we will reprogram the one-armed bandit game quite a few times. This is not the most exciting prospect, but it will give us a simple game that you already know how to program, so we can concentrate on lists and for loops. Grab the [exercise notebook](notebooks/One-armed bandit.ipynb) before we start.


## Chapter concepts
* Storing many items in [lists](#lists).
* Iterating over items using [for](#for-loop) loop.
* Building [range](#range) of values.
* Looping over [enumerated](#enumerate) indexes and values.
* Building lists via [list comprehension](#list-comprehension).

## Lists {#lists}
So far, we were using variables to store single values: computer's pick, player's guess, number of attempts, PsychoPy window object, etc. But sometimes we need to handle more than one value. We already had this problem in the [computer-based Guess-the-Number](#guess-the-number-ai) game when we needed to store the remaining number range. We got away by using two variables, one for the lower and one for the upper limit. However, this approach clearly does not scale well and, sometimes, we might not even know how many values we will need to store. Python's [lists](https://docs.python.org/3/library/stdtypes.html#lists) are the solution to the problem.

A list is a mutable^[More on that and tuples, list's immutable cousins, later.] sequence of items where individual elements can be accessed via their zero-based index. Extending the idea of [variable-as-a-box](#variables), you can think about lists as a box with numbered slots. To store and retrieve a particular piece you will need to know both the _variable name_ and the _index of the item_ you are interested in within that box. Then, you work with a variable-plus-index in exactly the same way you work with a normal variable, accessing or changing its value via the same syntax as before.

A list is defined via square brackets `<variable> = [<value1>, <value2>, ... <valueN>]`. An individual slot within a list is also accessed via square brackets `<variable>[<index>]` where index is, again, **zero-based**^[This is typical for "classic" programming languages but less so for ones that are linear algebra / data science oriented. Both Matlab and R use one-based indexing, so you need to be careful and double-check whether you are using correct indexes.]. This means that the _first_ item is `variable[0]` and, if there are _N_ items in the list, the last one is `variable[N-1]`. You can figure out the total number of items in a list by getting its length via a special [len()](https://docs.python.org/3/library/functions.html#len) function. Thus, you can access the last item via `variable[len(variable)-1]`^[There is a simpler way to do this, which you will learn in a little while.]. Note the `-1`: If your list has 3 items, the index of the last one is 2, if it has 100, then 99, etc. I am spending so much time on this because it is a fairly common source of confusion.

::: {.practice}
Do exercise #1 see how lists are defined and indexed.
:::

Lists also allow you access more than one slot/index at a time via [slicing](https://docs.python.org/3/library/functions.html#slice). You can specify index of elements via `<start>:<stop>` notation. For example, `x[1:3]` will give you access to two items with indexes 1 and 2. Yes, _two_ items: Slicing index goes from the `start` up to **but not including** the `stop`. Thus, if you want to get _all_ the items of a list, you will need to write `x[0:length(x)]` and, yet, to get the last item alone you still write `x[len(x)-1]`. Confusing? I think so! I understand the logic but I find this stop-is-not-included to be counterintuitive and I still have to consciously remind myself about this. Unfortunately, this is a standard way to define sequences of numbers in Python, so you need to memorize this.

::: {.practice}
Do exercise #2 to build the intuition.
:::

When slicing, you can omit either `start` or `stop`. In this case, Python will assume that a missing `start` means `0` (the index of the first element) and missing `stop` means `len(<list>)` (so, last item is included). If you omit _both_, e.g., `my_pretty_numbers[:]` it will return all values, as this is equivalent to `my_pretty_numbers[0:len(my_pretty_numbers)]`.^[Note, that this is almost but not quite the same thing as just writing `my_pretty_numbers`, as `my_pretty_numbers[:]` returns a _different_ list with _identical_ content. The difference is subtle but important and we will return to it later when talking about mutable versus immutable types.]

::: {.practice}
Do exercise #3.
:::

You can also use _negative_ indexes that are computed relative to length of the list^[If you are coming from R, negative indexing is completely different in Python.]. For example, if you want to get the _last_ element of the list, you can say `my_pretty_numbers[len(my_pretty_numbers)-1]` or just `my_pretty_numbers[-1]`. The last-but-one element would be `my_pretty_numbers[-2]`, etc. You can use negative indexes for slicing but keep in mind the _including-the-start-but-excluding-the-stop_ catch: `my_pretty_numbers[:-1]` will return all but last element of the list not the entire list!

::: {.practice}
Do exercise #4.
:::

Slicing can be extended by specifying a `step` via `start:stop:step` notation. `step` can be negative, allowing you to build indexes in the reverse order:

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers[4:0:-1]
#> [5, 4, 3, 2]
```

However, you must pay attention to the sign of the step. If it goes in the wrong direction then `stop` cannot be reached, Python will return an empty list.

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers[4:0:1]
#> []
```

Steps can be combined with omitted and negative indexes. To get every _odd_ element of the list, you write `my_pretty_numbers[::2]`:  

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers[::2]
#> [1, 3, 5, 7]
```

::: {.practice}
Do exercise #5.
:::

If you try to to access indexes _outside_ of a valid range, Python will raise an [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)^[If you are familiar with R and its liberal attitude towards indexes, you will find this very satisfying.]. Thus, trying to get 6^th^ element (index 5) of a five-element-long list will generate a simple and straightforward error. However, if your _slice_ is larger than the range, it will be truncated without an extra warning or an error. So, for a five-element list `my_pretty_numbers[:6]` or `my_pretty_numbers[:600]` will both return all numbers (effectively, this is equivalent to `my_pretty_numbers[:]`). Moreover, if the slice is empty (`2:2`, cannot include 2 because it is a stop value, even though it starts from 2 as well) or the entire slice is outside of the range, Python will return an empty list, again, neither warning or error is generated.

::: {.practice}
Do exercise #6.
:::

In Python lists are dynamic, so you can always add or remove elements to it, see [the list of methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). You can add a new item to the of the end of the list via `.append(<new_value>)` method

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.append(10)
my_pretty_numbers
#> [1, 2, 3, 4, 5, 6, 7, 10]
```

Or, you can `insert(<index>, <new_value>)` _before_ an element with that index. Unfortunately, this means that you can use an arbitrary large index and it will insert a new value as a _last_ element without generating an error.

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.insert(2, 10)
my_pretty_numbers.insert(500, 20)
my_pretty_numbers
#> [1, 2, 10, 3, 4, 5, 6, 7, 20]
```

You can remove an item using its index via `pop(<index>)`, note that the item is _returned_ as well. If you omit the index, `pop()` removes the _last_ element of the list. Here, you can only use valid indexes.

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.pop(-1)
#> 7
my_pretty_numbers.pop(3)
#> 4
my_pretty_numbers
#> [1, 2, 3, 5, 6]
```

::: {.practice}
Do exercise #7.
:::

## Reimplementing one-armed bandit game via lists
Phew that was _a lot_ about lists^[And we barely scratched the surface!]. However, [All work and no play makes Jack a dull boy](https://en.wikipedia.org/wiki/All_work_and_no_play_makes_Jack_a_dull_boy)! Let us return to the one-armed bandit game that you already implemented but refactor it using lists. The latter make a lot of sense when working with multple slots. Recall the rules: you have three slots with [random numbers](https://docs.python.org/3/library/random.html#random.randint) between 1 to 5, if all three number match you output "Three of a kind!", if only two numbers match you print "A pair!". Implement this game using a list instead of three variables. In the first version, use `<variable> = [<value1>, <value2>, ..., <valueN>] ` notation to define it. Also note that when using [string formatting](#string-formatting), you 
pass all values in a tuple (a frozen list, more on that in later chapters) or a list. Good news: your three values are in the list, so you can past to the string formatting, just think about the number of slots you need to define within the format string.

I know it will be tempted to just copy-paste-edit the code you already implemented by we are here to learn, so I strongly suggest writing it from scratch. It is a very simple program, redoing it is very easy but helps you practice more.

::: {.program}
Put your code into _code01.py_.
:::

Now, do the same but starting with an empty list and [appending](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) random numbers to it.

::: {.program}
Put your code into _code02.py_.
:::

## For loop{#for-loop}
In the code above, we needed to iterate over three moles (circles) that we had in a list. Python has a tool just for that: a
[for loop](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements) that iterates over the items in any sequence (our list is a sequence!). Here is an example:

```python
numbers = [2, 4, 42]
for a_number in numbers:
    print("Value of a_number variable on this iteration is %d"%(a_number))
    a_number = a_number + 3
    print("  Now we incremented it by 3: %d"%(a_number))
    print("  Now we use in a formula a_number / 10: %g"%(a_number / 10))
#> Value of a_number variable on this iteration is 2
#>   Now we incremented it by 3: 5
#>   Now we use in a formula a_number / 10: 0.5
#> Value of a_number variable on this iteration is 4
#>   Now we incremented it by 3: 7
#>   Now we use in a formula a_number / 10: 0.7
#> Value of a_number variable on this iteration is 42
#>   Now we incremented it by 3: 45
#>   Now we use in a formula a_number / 10: 4.5
```

Here, the code inside the `for` loop is repeated three times because there are three items in the list. On each iteration, next value from the list gets assigned to a temporary variable `a_number` (see the output). Once the value is assigned to a variable, you can use it just like any variable. You can print it out (first `print`), you can modify it (second line within  the loop), use its value for when calling other functions, etc. To better appreciate this, copy-paste this code into a temporary file (call it `test01.py`), put a [breakpoint](#debugging) onto the first `print` statement and then use **F10** to step through the loop and see how value of `a_number` variable changes on each iteration and then it gets modified in the second line within the loop.

Note that you can use the same [break](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#break-and-continue-statements-and-else-clauses-on-loops) statement as for the [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) loop.

::: {.rmdnote .practice}
Do exercise #8.
:::

## Using for loop to create slots
Use [for loop](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements) twice. First, when you are creating the three slots: Start with an empty list and append three random number using for loop. Second, when printing out the slots. I have pointed out above that having three values in a list makes it easier to do formatting but here, for the sake of exercise, print each slot separately using a for loop.

::: {.program}
Put your code into _code03.py_.
:::

## range() function: Repeating code N times{#range}
Sometimes, you might need to repeat the code several times. For example, imagine that you have 40 trials in an experiment. Thus, you need to repeat a trial-related code 40 times. You can, of course, build a list 40 items long by hand and iterate over it but Python has a handy [range()](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#the-range-function) function for that. `range(N)` yields N integers from 0 to N-1 (same up-to-but-not-including rule as for slicing) that you can iterate over in a for loop. 

```python
for x in range(3):
    print("Value of x is %d"%(x))
#> Value of x is 0
#> Value of x is 1
#> Value of x is 2
```

You can modify [range()](https://docs.python.org/3/library/stdtypes.html#range) function behavior by providing a starting value and a step size. But in its simplest form `range(N)` is a handy tool to repeat the code that many times. Note that while you always need to have a temporary variable in a `for` loop, sometimes you may not use it at all. In cases like this, you should use `_` (underscore symbol) as a variable name to indicate the lack of use.

```python
for _ in range(2):
    print("I will be repeated twice!")
#> I will be repeated twice!
#> I will be repeated twice!
```

Alternatively, you can use `range()` to loop through indexes of a list (remember, you can always access an individual list item via `var[index]`). Do exactly that^[Note, this is not a _better_ way but an _alternative_ way to do this.]! Modify your code to use [range()]((https://docs.python.org/3/library/stdtypes.html#range)) function in the for loop (how can you compute the number of iterations you need from the length of the list?), use temporary variable as an _index_ for the list to draw each item^[Style hint: if a variable is an _index_ of something, I tend to call it `isomething`. E.g., if it holds an index to a current mole, I would call it `imole`. This is _my_ way of doing it. Others use `i_` prefix or an `_i` suffix. But either way, it is a useful naming convention. Remember, the easier it is to understand the meaning of a variable from its name, the easier it is for you to read and modify the code.]. When in doubt, put a breakpoint inside (or just before) the loop and step through your code to understand what values a temporary loop variable gets and how it is used.

## Adding information on the slot index
In the previous version of the game, we had no way of telling the slot index. It is obvious from the order within the print out but it would be nicer if we explicitly would print out `"Slot #1: 2"`. Use [range()](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#the-range-function) function to generate indexes of slots, loop over these indexes and print out in "Slot #<slot-index> : <slot-value-for-that-index>". Note, however, that indexes in Python are zero-based but out slots start at 1 (no slot zero!). Think how it fix this in a print out.

::: {.program}
Put your code into _code04.py_.
:::

## Looping over both index and item via  list enumeration  {#enumerate}
It happens fairly often that you need to loop over both indexes and items of the list, so Python has a handy function for this: [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)! If, instead of iterating over a list, you iterate over [enumerate(<list>)](https://docs.python.org/3/library/functions.html#enumerate), you get a tuple with both `(index, value)`. Here is an example:

```python
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print('%d: %s'%(index, letter))
#> 0: a
#> 1: b
#> 2: c
```

Use [enumerate](https://docs.python.org/3/library/functions.html#enumerate) to loop over both index and item and print out one slot at a time. Look at the `start` parameter of the function to make sure your index now starts at 1.

::: {.program}
Put your code into _code05.py_.
:::

## List comprehension {#list-comprehension}
List comprehension provides an elegant and easy-to-read way to create, modify and/or filter elements of the list creating a new list. The general structure is
```python
new_list = [<transformation-of-the-item> for item in old_list if <condition-given-the-item>]
```
Let us look at examples to understand how it works. Imagine that you have a list `numbers = [1, 2, 3]` and you need increment each number by 1^[A very arbitrary example!]. You can do it by creating a new list and adding 1 to each item in the <transform-the-item> part:

```python
numbers = [1, 2, 3]
numbers_plus_1 = [item + 1 for item in numbers]
```

Note that this is equivalent to
```python
numbers = [1, 2, 3]
numbers_plus_1 = []
for item in numbers:
    numbers_plus_1.append(item + 1)
```

Or, imagine that you need to convert each item to a string. You can do it simply as
```python
numbers = [1, 2, 3]
numbers_as_strings = [str(item) for item in numbers]
```
What would be an equivalent form using a normal for loop? Write both versions of code in Jupiter cells and check that the results are the same.

::: {.rmdnote .practice}
Do exercise #9 in Jupyter notebook.
:::

Now, implement the code below using list comprehension. Check that results match.
```python
strings = ['1', '2', '3']
numbers = []
for astring in strings:
    numbers.append(int(astring) + 10)
```

::: {.rmdnote .practice}
Do exercise #10 in Jupyter notebook.
:::

As noted above, you can also use a conditional statement to filter which items are passed to the new list. In our numbers example, we can retain numbers that are greater than 1
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item for item in numbers if item > 1]
```

Sometimes, the same statement is written in three lines, instead of one, to make reading easier:
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item 
                          for item in numbers
                          if item > 1]
```

You can of course combine the transformation and filtering in a single statement. Create code that filters out all items below 2 and adds 4 to them.

::: {.rmdnote .practice}
Do exercise #11 in Jupyter notebook.
:::

## Using list comprehension to create three slots
Let us use list comprehension to build three slots in a single line. The good news, we spare ourselves creating an empty list and use of `append`. The bad news, you need to think about which values you want to loop over if you want to create three random numbers. Hint, look at [range()](#range) function again and think whether you will be actually using the temporary loop variable. 


::: {.program}
Put your code into _code06.py_.
:::

