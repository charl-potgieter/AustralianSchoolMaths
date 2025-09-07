class Class_A:
    @property
    def my_value(self) -> int:
        return 1

    def my_print(self):
        print(self.my_value)


class Class_B(Class_A):
    @property
    def my_value(self) -> int:
        return 2


if __name__ == "__main__":
    a = Class_A()
    a.my_print()

    b = Class_B()
    b.my_print()
