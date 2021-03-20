# Introduction

Telegram bots are very powerful piece of softwares. They act as an easy-to-use point of access for any kind of service by simulating a conversation with an automated user. Said so, a lot of bots share a consistent subset of features, that result simple but still a lot appreciated by final users.

A trivial example are [welcome messages](https://github.com/PyTG/pytg-welcome-message), sent by a brandized bot when a user joins the community's group. While the text of the message changes based on the context, the Python's code needed is exactly the same. Using PyTG, the operation of adding such a feature consists in adding a module and modifying the message's format.

Sometimes bots need to interface with different services than Telegram, interacting with their APIs. In these cases, a module may act as a wrapper for those requests (take a look at the [sheets](https://github.com/PyTG/pytg-sheets) module).

Each module is loaded independently at startup, but this doesn't mean that they're put in an airlock. Each module may send a message to another one, and PyTG operates as a broker to deliver the request. A deeper analysis of the communication mechanism and some code examples are shown in the next sections.