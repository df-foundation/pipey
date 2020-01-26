<p align="center">
  <img src="https://github.com/dataframehq/pipey/raw/master/docs/_static/img/Pipey.png?raw=true" height="90px">
</p>

![](https://github.com/dataframehq/pipey/workflows/Python%20CI/badge.svg)


---

`pipey` is an open source framework that provides **declarative syntactical sugar** within python. For those familiar with the R tidyverse ecosystem, `pipey` facilitates magrittr-style piping using the right bitshift operator `>>`, while staying largely pythonic in implementation. Unlike other `pandas`-oriented systems (e.g. [dfply](https://github.com/kieferk/dfply) or [pandas-ply](https://github.com/coursera/pandas-ply)), `pipey` is meant to be flexible, and therefore does not enforce any particular object input types, while providing additional custom functionality.


## Installation
```
pip install pipey
```

## Usage

The entirety of `pipey`'s functionality can be captured in the `pipey.Pipeable` class, which can be passed a function to create a Pipeable-compatible function or used as a decorator around a new function. Both of these functionalities are shown below.

<p align="center">
  <img src="https://github.com/dataframehq/pipey/raw/master/docs/_static/img/example.png?raw=true" height="300px">
</p>


`pipey` is meant to be flexible, and therefore can accept \(almost\) anything as input. Creating custom functions compatible with the `pipey` framework is therefore quite easy, as long as an existing `__rshift__` method doesn't exist for the object being passed to `Pipeable`.


## Extended usage

We support keyword arguments (and decorators, for convenience) to extend the basic piping functionality.

See `extended.py` for the full set of decorators.


### Accept multiple inputs

By default, the input is passed as the first argument of the receiving function, but `Pipeable` allows multiple inputs to be passed in as a tuple or list through the keyword argument `unpack_input`, as shown below.

```
Print = Pipeable(print, unpack_input=True)

('hello', 'world') >> Print

> hello world
```

### Use only first input

Often functions will return a tuple of outputs, and when chaining `Pipeable`-compatible functions together, it's convenient to only take the first argument. This can be accomplished with the keyword argument `use_first_arg_only` as follows:

```
Print = Pipeable(print, use_first_arg_only=True)

('hello', 'world') >> Print

> hello
```

### Enable calling

To remain unambiguous, by default we disable `Pipeable`-decorated objects to be called normally -- i.e. they can only be called through the piping syntax, with `>>`. This prevents unintended behavior when a function only has optional named parameters, in which case the Pipeable function would be called before the `>>` operation had a chance to pipe an input.

Nonetheless, we support traditional calling of our Pipeable functions using the keyword argument `use_first_arg_only`, though we urge you to **have at least one required positional argument in your function definition** to ensure this behaves as intended. This behavior can be enables as follows:

```
Print = Pipeable(print, try_normal_call_first=True)

Print('hello world')

> hello world
```

### Append docstring

We supply an `append_docstring` decorator to allow docstrings from other functions to be bolted onto Pipeable docstrings. This can be invoked as a decorator, as follows:

```
@append_docstring(print)
@Pipeable
def Print(*args, **kwargs):
    print(*args, **kwargs)
```


