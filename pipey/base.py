class Pipeable():
    """Class that enables `>>` to function as a piping operator.
    """

    def __init__(self, base_object=None, *args, unpack_input=False, use_first_arg_only=False, try_normal_call_first=False, **kwargs):
        self.__doc__ = base_object.__doc__
        self.base_object = base_object
        self.args = args
        self.kwargs = kwargs
        self.unpack_input = unpack_input
        self.use_first_arg_only = use_first_arg_only
        self.try_normal_call_first = try_normal_call_first

    def __rshift__(self, other):
        return other.base_object(self.base_object, *other.args, **other.kwargs)

    def __rrshift__(self, other):
        if self.unpack_input:
            return self.base_object(*other, *self.args, **self.kwargs)
        elif self.use_first_arg_only:
            return self.base_object(other[0], *self.args, **self.kwargs)
        else:
            return self.base_object(other, *self.args, **self.kwargs)

    def __getattr__(self, attribute):
        return getattr(self.base_object, attribute)

    def __call__(self, *args, **kwargs):
        if self.try_normal_call_first:
            try:
                return self.base_object(*args, **kwargs)
            except:
                pass
        if self.base_object is not None:
            # Typical behavior: Pipeable object is created when the Pipeable object is called, allowing for functions to be defined.
            return Pipeable(
                self.base_object,
                *args,
                unpack_input=self.unpack_input,
                use_first_arg_only=self.use_first_arg_only,
                try_normal_call_first=self.try_normal_call_first,
                **kwargs
            )
        else:
            # Pipeable was created with no base_object, so enable use of Pipeable object as a decorator.
            return Pipeable(
                *args,
                unpack_input=self.unpack_input,
                use_first_arg_only=self.use_first_arg_only,
                try_normal_call_first=self.try_normal_call_first,
                **kwargs
            )

