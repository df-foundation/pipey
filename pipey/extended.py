import textwrap

def unpack_input(pipeable):
    """Decorator to place before Pipeable to cause inputs to be unpacked into the Pipeable-decorated function.

    I.e. if you want (a, b) >> func() to correspond to func(a, b), then place this above Pipeable, as follows::

        @unpack_input
        @Pipeable
        def func(a, b):
            pass

    """
    pipeable.unpack_input = True
    return pipeable


def use_first_arg_only(pipeable):
    """Decorator to place before Pipeable to cause only first input to be used.

        @use_first_arg_only
        @Pipeable
        def func(a, b):
            pass

    """
    pipeable.use_first_arg_only = True
    return pipeable


def try_normal_call_first(pipeable):
    """Decorator to place before Pipeable to enable the Pipeable object to be called normally. The base function must have one required position parameter.

        @try_normal_call_first
        @Pipeable
        def func(a, b):

    """
    pipeable.try_normal_call_first = True
    return pipeable


def append_docstring(original_function):
    """Decorator to append the docstring of `original_function` to a function before passing to Pipeable.

        @append_docstring(dir)
        @Pipeable
        def Dir(*args, **kwargs):
            return dir(*args, **kwargs)

    """
    doc_to_append = original_function.__doc__
    def wrapper(func):
        header = '`{}` docstring'.format(original_function.__name__)
        header += '\n\t' + len(header)*'-'
        header = '\n\t' + header + '\n'

        header = textwrap.dedent(header)

        # Deal with empty docstring.
        if func.__doc__ is not None:
            func.__doc__ += header
        else:
            func.__doc__ = header

        func.__doc__ += doc_to_append
        return func
    return wrapper

