# The `setUp` method

Interestingly, this method in the `unittest` library is called `setUp()`, and **not** `set_up()` as you would expect in Python.

This method runs for each test—so before each test you run the `setUp()` method.

After each test, a `tearDown()` method runs. We have not defined such method in this code.

## Class-level setUp

If you'd like a method to run once for the entire `TestCase`, you can use `setUpClass()` instead. That only runs once for all the test methods within the test case.

Similarly, a `tearDownClass()` method is also available.