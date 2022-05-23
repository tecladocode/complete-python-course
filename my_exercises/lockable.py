class LockableList:
    def __init__(self, *values, locked=False):
        self.values = list(values)
        self._locked = locked

    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        values = ", ".join([value.__repr__() for value in self.values])
        return f"LockableList({values})"
    # LockableList(['Rolf', 'John', 'Anna'])

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        if isinstance(i, int):
            # Perform conversion to positive index if necessary
            if i < 0:
                i = len(self.values) + i

            # Check index lies within the valid range and return value if possible
            if i < 0 or i >= len(self.values):
                raise IndexError("LockableList index out of range")
            else:
                return self.values[i]
        elif isinstance(i, slice):
            start, stop, step = i.indices(len(self.values))
            rng = range(start, stop, step)
            return LockableList(*[self.values[index] for index in rng])
        else:
            invalid_type = type(i)
            raise TypeError(
                "LockableList indices must be integers or slices, not {}".format(
                    invalid_type.__name__)
            )

    def __setitem__(self, i, values):
        if self._locked == True:
            raise RuntimeError(
                "LockableList object does not support item assignment while locked"
            )
        if isinstance(i, int):
            # Perform conversion to positive index if necessary
            if i < 0:
                i = len(self.values) + i

            # Check index lies within the valid range and assign value if possible
            if i < 0 or i >= len(self.values):
                raise IndexError("LockableList index out of range")
            else:
                self.values[i] = values
        elif isinstance(i, slice):
            start, stop, step = i.indices(len(self.values))
            rng = range(start, stop, step)
            if step != 1:
                if len(rng) != len(values):
                    raise ValueError(
                        "attempt to assign a sequence of size {} to extend a slice of size {}".format(
                            len(values), len(rng))
                    )
                else:
                    for index, value in zip(rng, values):
                        self.values[index] = value
            else:
                self.values = self.values[:start] + values + self.values[stop:]
        else:
            invalid_type = type(i)
            raise TypeError(
                "LockableList indices must be integer or slices, not {}".format(
                    invalid_type.__name__)
            )

    def __add__(self, other):
        if isinstance(other, (list, LockableList)):
            return LockableList(*(self.values + other))

        invalid_type = type(other)
        raise TypeError(
            'can only concatenate list or LockableList (not "{}") to LockableList'
            .format(invalid_type.__name__)
        )

    def __radd__(self, other):
        if isinstance(other, (list, LockableList)):
            return LockableList(*(other + self.values))

        invalid_type = type(other)
        raise TypeError(
            'can only concatenate list or LockableList (not "{}") to LockableList'
            .format(invalid_type.__name__)
        )

    def __iadd__(self, other):
        if self._locked:
            raise RuntimeError(
                "LockedList object does not support in-place concatenation while locked"
            )

        if isinstance(other, (list, LockableList)):
            self.values = self.values + other
            return self

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False


my_lock_list_1 = LockableList(1, 2, 3, 4, 5)
my_lock_list_2 = LockableList(6, 7, 8, 9, 10)
my_lock_list_3 = [6, 7, 8, 9, 10]
my_lock_list_1 += my_lock_list_3
print(type(my_lock_list_1))
print((my_lock_list_1))
my_lock_list_3 += my_lock_list_2
print(type(my_lock_list_3))
print((my_lock_list_3))
print(type(my_lock_list_1 + my_lock_list_3))
print(my_lock_list_1 + my_lock_list_3)
print(type(my_lock_list_3 + my_lock_list_1))
print(my_lock_list_3 + my_lock_list_1)
