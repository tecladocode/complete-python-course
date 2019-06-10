# Boundary Value Analysis

When you're testing a function such as our `divide`, it is unnecessary to test all possible values as inputs.

But which values should you test?

Through careful thinking and experience, we can identify boundaries in the inputs. For example, our `divide` has a boundary at the number `0`. It behaves significantly differently with values `-1`, `0`, and `1`.

Testing the boundaries and values around the boundaries is helpful and can help identify problems.

Just the act of *thinking* about these boundaries can sometimes be the even more helpful exercise though, as it can help you design your code better by realising where problems might happen!

## Should you test values other than boundaries?

Definitely. You can test a few different values within each group (groups are called *equivalence classes*). Doing this ensures that the test isn't just working because of a input and output combination.

For example, if your divide function looks like this:

```python
def divide(dividend, divisor):
    return 5
```

Then a test like this would work:

```python
def test_divide(self):
    self.assertEqual(divide(25, 5), 5)
```

But naturally, you can see how the function isn't really doing what you would expect. This is why having multiple tests, or trying various inputs within an equivalence class and at the boundaries, can be helpful.
