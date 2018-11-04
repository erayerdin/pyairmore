# Custom Requests

`AirmoreRequest` is a custom `PreparedRequest` class which handles requesting
to an Airmore server. It is intended to be an abstract class, which is not to
be initialized, but extended. Further examples will be provided.

It overrides the methods of `PreparedRequest` below:

 - `__init__`
 - `prepare_method`
 - `prepare_url`

## Initialization

Initialization of `AirmoreRequest` will take an `AirmoreSession` instance and
stored in private `__session` property.

    request = AirmoreRequest(session)

## Preparing Method

`prepare_method` method of an `AirmoreRequest` object will *always* changes
`url` property to `POST` since Airmore server always uses `POST` method to
communicate with a client. It is also called on super initialization
automatically.

## Preparing URL

`prepare_url` method will prepend `base_url` property of `AirmoreSession`
instance, which means:

    request.prepare_url("/foo", {})
    # will change `request.url` to "http://host:port/foo
    
    request.prepare_url("/foo", {"bar": "baz"})
    # will change it to "http://host:port/foo?bar=baz

## Extending `AirmoreRequest`

As told above, `AirmoreRequest` is to be extended rather than initialized.
If you want to have a custom behavior on an Airmore endpoint, see below:

    class ExampleRequest(AirmoreRequest):
        def __init__(self, session, foo):
            super().__init__(session)
            self.prepare_url("/bar")
            self.prepare_body(data=None, files=None, json={"foo": foo})

Then, you can pass the instance of your extended class into `send` method of
an `AirmoreSession` instance.

    request = ExampleRequest(session, foo=True)
    response = session.send(request)
    # will send a POST request to "http://host:port/bar
    # with a JSON body: {"foo": true} 

`AirmoreRequest` has many implementations in `pyairmore.services.*` so you
will not be likely to do this.
