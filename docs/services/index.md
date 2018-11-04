# Introduction

`Service` instance, simply, contains a `AirmoreSession` instance and helping
functions. While you can also extend `Service` class, `pyairmore` contains
many predefined `Service`s and `AirmoreRequest`s in order to make common actions
easier.

You can pass to a subsection, the rest of this page contains information for
the ones who want to develop `pyairmore` or who are curious about it.

## Creating A Custom Service

To create a custom service, you will need to extend two classes: `Service`
(naturally) and `AirmoreRequest` (at least once).

Creating a [custom request][custom_request] was already discussed. We will use
that example.

[custom_request]: ../requesting-and-session/custom-requests/#extending-airmorerequest

To create a custom service, simply do:

    class ExampleService(Service):
        def __init__(session):
            super().__init__(session)

Now, we need to create a method that does *something*. We will call it
`fetch_bar` in this example. Before doing anything else in this function:

1. We will create an `ExampleRequest` instance.
2. Pass that instance to `send` method of `session` property.

To do these:

    class ExampleService(Service):
        def __init__(session):
            super().__init__(session)
        
        def fetch_bar(foo):  # a custom method
            # the things we do first
            request = ExampleRequest(self.session, foo)
            response = self.session.send(request)

            # then do whatever you want, use `response`

Then we can call `fetch_bar`:

    service = ExampleService(session)
    service.fetch_bar(5)  # whatever it returns

This is how you create a custom service. Again, you will not probably do that
since `pyairmore` may already contain prebuilt `Service`s.
