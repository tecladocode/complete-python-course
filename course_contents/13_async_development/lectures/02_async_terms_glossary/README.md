---
hidden: true
---

# Glossary of terms used in concurrency

Hey there! Welcome to one of the most advanced topics in Python. A lot of developers are scared of what we're going to learn in this section.

You shouldn't be scared!

We'll start at the fundamentals, and build out our knowledge of asynchronous development from the ground up.

Throughout the section we'll learn more about what these terms mean, but it can be helpful to have a short glossary of terms just in case you want to come back and remind yourself.

- **Synchronous**: actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.
- **Asynchronous**: actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").
- **Concurrency**: The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.
- **Parallelism**: Running two or more things at the same time.
- **Thread**: A line of code execution that can run in one of your computer's cores.
- **Process**: One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).
- **GIL**: A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.

Take it slowly through this section, and ask questions in the Course Q&A as required. We're here to help!

Kind regards,

Jose