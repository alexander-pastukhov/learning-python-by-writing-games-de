# Sudoku {#Sudoku}

In this chapter, we are going to write programs that will both generate and solve [sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku). In this puzzle, you need to complete a $9\times9$ grid with number 1 to 9, so that number do not repeat within each row, each column, and each $3\times3$ square block. When you play the game, you have an incomplete puzzle and the more gaps you have, the harder the puzzle tends to be. But before you can play the game, some (that is you, today) must 1) generate a complete puzzle, 2) remove some numbers while ensuring that the solution to the puzzle remains unique.

The puzzle is based on a 2D grid and, in principles, you can use [list](#lists) of rows (which are lists themselves) to create this grid. This would be similar to the list of lists that contained information about connecting caves in (Hunt the Wumpus)[#hunt-the-wumpus] game. However, this nested list structure makes it hard to work with columns and blocks, as their elements belong to different lists, so you need to use for loop instead of simpler list slicing (works, but only for rows).

Instead, we will use it as an opportunity to learn about [NumPy](https://numpy.org/) library, which is one of the key packages for scientific computing in Python and is a foundation for many data analysis libraries. Note that the material below is by no means complete. If anything, it barely scratches the surface of NumPy. If you need NumPy for your projects, I strongly recommend taking a look at offical [Getting Started for aboslute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) guide and the official [user guide](https://numpy.org/doc/stable/user/index.html).

## Importing NumPy
The NumPy is not a core Python library, so you may need to [install it](https://numpy.org/install/). As with all libraries, you must import NumPy before using it in your script. However, this is one of the rare cases where renaming the library during import is a standard and recommended way:

```python
import numpy as np
```

## 1D NumPy arrays versus Python lists
The key data structure that NumPy introduces is a NumPy array that can have any number of dimensions. A one dimensional array, typically called "a vector", is most directly related to a Python [list](#lists), but with both some limitations and some extra functionality. Unlike Python lists that can hold anything, including other lists, all elements of an array must be of the same [numeric type](https://numpy.org/doc/stable/user/basics.types.html) (but [character arrays](https://numpy.org/doc/stable/reference/generated/numpy.chararray.html) can be created as well). However, the advantage of this restriction is that since all elements are of the same type, it is guaranteed that you can apply the same function to all the elements. Note that there is no such guarantee for potentially heterogenous Python lists, which is why you need to perform operation on each element separately. 

You can create a Numpy array from a list via [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) function:

```python
import numpy as np

# A Python list of numbers
a_list = [1, 5, 7]
print(a_list)
#> [1, 5, 7]

# A NumPy array created from the list
an_array = np.array(a_list)
print(an_array)
#> [1 5 7]
```

Note that because of "all values must be of the same type restriction", if the original Python list contained data of various types, all values will be converted to the most flexible one. E.g., a mix of logical values and integers will give you integers, a mix of integers and floats will give you all floats, a mix of anything with strings will give you strings, etc.


```python
# logical and integers -> all integers
print(np.array([True, 2, 3, False]))
#> [1 2 3 0]

# integers and floats -> all floats
print(np.array([1.0, 2, 3, 0.0]))
#> [1. 2. 3. 0.]

# logica, integers, floats, and strings -> all strings
print(np.array([False, 1, 2.0, "a"]))
#> ['False' '1' '2.0' 'a']
```

However, note that the type of an array is fixed at the creation type and if you put in a different type value, it will be either converted to that type or, if conversion is tricky, NumPy will throw an error.

```python
# array of boolean
array_of_bool = np.array([True, False, True])

# float value is automatically converted to logical
# it is True because only 0.0 is False
array_of_bool[1] = 2.0
print(array_of_bool)
#> [ True  True  True]

# an arbitrary string value that cannot be converted automatically to an integer
array_of_int = np.array([1, 2, 3])
array_of_int[1] = "A text"
#> invalid literal for int() with base 10: 'A text'
```

::: {.practice}
Do exercise #1.
:::

In general, what you can can do with a list, you can do with a NumPy 1D array. For example, slicing works the same way, you can loop over elements of an array the same way, etc.

```python
a_list = [1, 5, 7]
an_array = np.array(a_list)

# slicing
print(a_list[:2])
#> [1, 5]
print(an_array[1:])
#> [5 7]

# for loop
for value in an_array:
  print(value)
#> 1
#> 5
#> 7
```

However, certain functionality is implemented differently, as the [append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy-append) in the example below. The other functionality, such as a [pop](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), is missing but can be emulated through slicing.


```python
# appending values
an_array = np.append(an_array, [4])
print(an_array)
#> [1 5 7 4]
```

The most important practical difference between lists and numpy arrays is that because the latter are homogenous, the operations on them are vectorized. This means that you apply a function to the entire array in one go, making it both easier to use and faster, as most operations on arrays are heavily optimized. Here is an example of multiplying and then adding the same value to all every array element, something that requires a for loop for a normal list

```python
a_list = [1, 2, 3]
an_array = np.array(a_list)
2 * an_array + 1
#> array([3, 5, 7])
```

You can also perform elementwise operations on two (or more) arrays at the same time. E.g., here is an example of elementwise addition for two arrays

```python
array1 = np.array([1, 2, 4])
array2 = np.array([-1, -3, 5])
array1 + array2
#> array([ 0, -1,  9])
```
Note that it works only if array [shapes](https://numpy.org/doc/stable/reference/generated/numpy.shape.html) are the same. In case of the 1D arrays (a.k.a., vectors), it means that their length must be the same. 

```python
array1 = np.array([1, 2, 4])
array2 = np.array([-1, -3, 5, 7])
array1 + array2
#> operands could not be broadcast together with shapes (3,)
#> (4,)
```

At the same time, you can always use vectors with a single element, which are called "scalars" and this single value is used for every element in the other vector.

```python
a_vector = np.array([1, 2, -4])
a_scalar = np.array([-1])
a_vector * a_scalar
#> array([-1, -2,  4])
```

::: {.practice}
Do exercise #2.
:::

Vectorization also means that you can apply aggregating function -- [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html), [median](https://numpy.org/doc/stable/reference/generated/numpy.median.html), [min](https://numpy.org/doc/stable/reference/generated/numpy.min.html), etc. --- to the array instead of computing it by hand.

::: {.practice}
Do exercise #3.
:::


## 2D NumPy arrays, a.k.a., matrices
The real power of NumPy is unleashed once your array have two or more dimensions. The 2D arrays are called matrices, whereas arrays with three or more dimensions are known as tensors. The former play key role in classic linear algebra in Python, whereas the latter are required for artifical neural networks (hence, tensor, in [TensorFlow](https://www.tensorflow.org/)).

As with vectors (1D arrays) versus Python lists, the advantage comes from restrictions. Matrices are rectangular, i.e., matrices are composed of multiple rows but each row has the same number of elements. In contrast, you _can_ create a rectangular matrix as list of lists (again, our `CONNECTED_CAVES` was $20\times3$ rectangular matrix) but this is not guaranteed. On top of that, homogenity of the matrix (all values must of the same type) means you can extract an rectangular part of the matrix and it is guaranteed to be another matrix of the same type. And slicing makes working with 2D arrays much easier. E.g., here is the code to extract a column from a list of lists versus NumPy matrix.


```python
matrix_as_list = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
matrix_as_array = np.array(matrix_as_list)

icolumn = 1 # column index that we want to extract

# extracting column from via for loop
column_as_list = []
for row in matrix_as_list:
  column_as_list.append(row[icolumn])
print(column_as_list)
#> [2, 5, 8]

# extracting column from a matrix
print(matrix_as_array[:, 1])
#> [2 5 8]
```

Extracting rows, columns, and square block out of a matrix will be key to writing the code for Sudoku, so lets practice!

::: {.practice}
Do exercise #4.
:::

## Creating arrays of a certain shape
There are different ways to create NumPy arrays. Above, we used lists or lists of lists to create them. However, you need create an array of a certain [shape](https://numpy.org/doc/stable/reference/generated/numpy.shape.html) filled with [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) or [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html). The key parameter in these functions is the _shape_ of the array: a list with its dimensions. For a 2D array this means `(<number of rows>, <number of columns>).


```python
zeros_matrix_3_by_2 = np.zeros((3, 2))
print(zeros_matrix_3_by_2)
#> [[0. 0.]
#>  [0. 0.]
#>  [0. 0.]]
```

::: {.practice}
Martix filled with 7.
Do exercise #5.
:::

## Creating random arrays of a certain shape
NumPy has a module for generating random number --- [numpy.random](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random) --- that is conceptually similar to the [random](https://docs.python.org/3/library/random.html) but allows you to generate arrays rather than single values. For convenience, the names are kept the same. E.g., function [random.randint](https://docs.python.org/3/library/random.html#random.randint) that generates a single random integer has its twin brother [numpy.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html) that accepts same parameters and, by default also generates a single value. However, you can generate the whole vector / matrix / tensor of random numbers in one go by spezifying its `size`. Confusingly, the parameter is called `size` even though it refers to the "output shape".

::: {.practice}
Generate random 4x5 matrix with normally distributed numbers with mean of 3 and standard deviation of 1. 
Do exercise #6.
:::

## Creating arrays with sequences
Similar to creating a range of integer values via [range](https://docs.python.org/3/library/functions.html#func-range), you can create a vector of integer values via [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)^[The name is confusing, but apparently this is a short for "array range"], although this is equivalent to `np.array(range(...))`:


```python
print(np.arange(5))
#> [0 1 2 3 4]
print(np.array(range(5)))
#> [0 1 2 3 4]
```
However, NumPy also has a handy function called [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) that allows you generate sequence of _float_ numbers. 

::: {.practice}
Generate random 4x5 matrix with normally distributed numbers with mean of 3 and standard deviation of 1. 
Do exercise #7.
:::

## Stacking array to create a matrix
The [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) function will be useful for us to generate a sequence of integers from 1 to 9. However, note that in both cases you can only generate a vector but not a matrix that we need! The solution in this case is to [stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html) individual vectors. When stacking, shapes of individual vectors starts to play a very important role. Unlike lists, that only have [length](https://docs.python.org/3/library/functions.html#len), all arrays including vectors have also [shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html): information about each dimension.

Things are easy for truly one dimensional arrays. These are arrays created from lists or via functions such as [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) or [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html). If you look at their [shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html), you will see just one dimension.


```python
print(np.array([10, 20, 30]).shape)
#> (3,)
print(np.zeros(5).shape)
#> (5,)
```

These vectors do not have "orientation" (more on this later), so when you combine these arrays into a matrix you can use them as rows (stacking along `axis=0`, the default, see also [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)) or as columns (stacking along `axis=1`, see also [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)). 



```python
one_d_vector = np.arange(5)

# Stacking vertically: vectors are used as rows
print(np.stack([one_d_vector, one_d_vector]))
#> [[0 1 2 3 4]
#>  [0 1 2 3 4]]
print(np.stack([one_d_vector, one_d_vector]).shape)
#> (2, 5)

# Stacking horizontally: vectors are used as columns
print(np.stack([one_d_vector, one_d_vector], axis=1))
#> [[0 0]
#>  [1 1]
#>  [2 2]
#>  [3 3]
#>  [4 4]]
print(np.stack([one_d_vector, one_d_vector], axis=1).shape)
#> (5, 2)
```


First, they can be either column or row vectors. A column vector is "vertical" relative to a 2D matrix, i.e., it correspond to a single column with values  distributed across the rows. Conversely, a row vector is "horizontal" and corresponds to a row of a matrix with its values going along columns. You can convert one to the another via [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html) function.
The difference between column and row vectors is extremely important role for linear algebra but in our case it determines the axis along which we can stack vectors to create a matrix. If vectors are column vectors, we need to stack them horizontaly, whereas for row vectors --- vertically.



If you specify a single 

```python
np.array([1, 2, 3]).shape
#> (3,)

column_vector = np.arange(5)
np.stack([column_vector, column_vector], axis=0)
#> array([[0, 1, 2, 3, 4],
#>        [0, 1, 2, 3, 4]])
```

