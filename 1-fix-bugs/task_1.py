class A:
    __slots__ = ("foo", "bar")

    foo: int
    bar: str = "hello\n"

    def __init__(self, foo, bar=None):
        self.foo = foo
        self.bar = bar if bar is not None else self.bar

    def multiple(self):
        return self.foo * self.bar


a = A(foo=2)

print(a.multiple())
