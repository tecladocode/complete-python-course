"""
Regular expressions are one of those topics that are usually covered plenty in online courses and tutorials, but never quite understood very well.

Through examples, hopefully you’ll end this video with a good understanding of what regular expressions are for, how to use them, and how to learn more when you get stuck (because you will, undoubtedly!).

The first thing to understand is that regular expressions are a language. Not a programming language, but a language nonetheless.

There’s a specific syntax and keywords that you can use in regular expressions to express what you want.

So what are regular expressions used for?

*We use regular expressions to specify patterns in text*.

For example, do you notice any patterns in this text?


a1 a3 a9 a5 a4


I notice a pattern here which is: an `a` followed by a number, followed by a space.

I notice another pattern, which is `a1 a3 a9 a5 a4` (that’s the entire string, followed by nothing). This will be the case for every example.

Here’s another example:


Jose, Rolf, Charlie, Adam


I notice a pattern here which is a set of characters, followed by a comma, followed by a space.

Here’s another pattern:


http://google.com
https://www.facebook.com
https://www.twitter.com
https://udemy.com
http://tecladocode.com


There’s two main patterns here:

* A set of characters followed by a newline character (remember the `\n`?);
* In each line, there’s:
	* `http`;
	* sometimes followed by an `s`;
	* followed by `://`;
	* sometimes followed by `www.`;
	* followed by a set of characters;
	* followed by `.com`.

What about these?


jose@tecladocode.com
rolf@google.com
char.lie@twitter.com
anna@gmail.com
jen45@icloud.me
someone_is_awesome@example.net


These are a bit more complex, but for each email here’s what I see:

* A set of a combination of (letters, numbers, periods, and underscores);
* Followed by `@`;
* Followed by some characters (seems only letters from this set);
* Followed by `.`;
* Followed by some characters (seems only `com`, `me`, and `net` from this set).

“Getting” regex will be a matter of you seeing these patterns and being able to express using regex syntax.

So you need two things:

* To see the pattern (sometimes, not so easy; sometimes, easy to miss corner cases);
* To be able to express the pattern using regex syntax.

I’ve given you a few examples of patterns, but really it requires time and analysing many patterns to be able to get quicker at this.

Now let’s look at the regex syntax. I won’t cover absolutely everything you can learn about regex (that would take an entire course!), but the main components.

The four most important are:

* `.`;
* `+`;
* `*`; and
* `?`

The `.` means “anything”; such as a letter, number, symbol, space, etc… *but not newline characters*.

The `+` means “one or more of”. The `*` means “zero or more of”. The `?` means “zero or one of”.

So `.+` means “one or more of anything”. `.*` means “zero or more of anything”. `.?` means “zero or one of anything”.

For the string:


jose@tecladocode.com


`.*` would match the pattern, since it’s “zero or more of anything”.

`Jose@tecladocode\.com` would also match the entire pattern, since it is the pattern. Notice the `\.` so that the `.` doesn’t mean “anything”. With the backslash in front, it matches the actual `.` character.

Next, we have *character sets*. This is a character set: `[abc]`. For this string:

`charlie`, `[abc]` would match the `c` and the `a`. For `Charlie` though it would only match the `a`—these are case sensitive.

Another important one is the *range*. It allows us to define a range of characters, such as a to z: `[a-z]`.

For `jose`, `[a-z]` would match every letter individually.

For `jose`, `[a-z]+` would match as many consecutive set of letters in that range as possible; that’s the entire word.

For `jo.se`, `[a-z]+` would match twice; `jo`, and `se`.

Let’s look at the e-mails.


[A-z]+@[a-z]+\.[a-z]+


Of course this one won’t match the periods or the underscores on the e-mail. Let’s fix it:


[A-z\._]+@[a-z]+\.[a-z]+


If instead of matching all TLDs (that’s `net`, `com`, me`) we wanted to match only the ones we’ve seen, we could do:


[A-z\._]+@[a-z]+\.(com|me|net)


There’s a lot more to regular expressions, but this will certainly get you started. http://regexr.com has more information, cheatsheets, and also the online editor for you to try things out.

If you have any problems with any regex expressions, feel free to post in the Slack channel for help (even if it’s unrelated to the course). We’ll be glad to help you out!
"""