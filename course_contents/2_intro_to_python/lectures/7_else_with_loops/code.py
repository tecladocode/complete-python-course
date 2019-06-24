# On loops, you can add an `else` clause. This only runs if the loop does not encounter a `break` or an error.
# That means, if the loop completes successfully, the `else` part will run.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")


# Remove the "faulty" and you'll see the `else` part starts running.
# Link: https://blog.tecladocode.com/python-snippet-1-more-uses-for-else/
