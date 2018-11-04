# How Session Works

`AirmoreSession` extends `Session` class which makes it automatic to authorize
on each `AirmoreRequest`.

In order to use a `Service`, you will need an `AirmoreSession` instance.

## Initialization

To initialize `AirmoreSession`, you will need an `IPv4Address` instance from
`ipaddress` module. Import `IPv4Addres`, create an instance, and then you can
create an `AirmoreSession` instance.

    from ipaddress import IPv4Address
    from pyairmore.request import AirmoreSession
    
    ip = IPv4Address("192.128.1.x")  # change to server's address
    session = AirmoreSession(ip)  # you can also pass a port as int, default to 2333

If you do not know target device's IP (and port), open Airmore on target device,
press menu button on top-right, press "Get IP" to see your IP and port.

## Validating Methods

These methods below are already automated on `send` method of your
`AirmoreSession` instance. You do not have to call these methods, but these
will give you insights about if target device is ready to accept requests.

### Is Server Running?

To check if server on target device is running, you will use `is_server_running`
property.

    session.is_server_running  # True

Server behavior depends on (i) target device's Android version and (ii) target
device's power since Airmore may shut down server due to low battery level.

### Is Application Open?

To check if Airmore application's main activity can be seen on device, you can
call `is_application_open` property.

    session.is_application_open  # False

 > #### Warning
 > This is the only method that is not called on `send` method of `AirmoreSession`
 > instance.

### Requesting Authorization

To use a `Service`, you will need to be authorized on target device. It is
automatically called on any `Service` method and `send` method as well. To
call it manually:

    session.request_authorization()  # True

If you are not authorized, a dialog will appear on target device's screen to
accept authorization. If you are already authorized, the server will return
`True`.

 > #### Warning
 > If you are not authorized, the dialog will appear on target device's screen
 > and this will *block* the current thread until target device accepts the
 > authorization.

 > #### Warning
 > On some devices, the device must be unlocked for authorization dialog to
 > appear. On some devices, it even needs Airmore application's main activity
 > to be open on front. This behavior is pretty inconsistent.
 > 
 > To be safe, you might call `is_application_open` before each action (it is
 > not called automatically). However, this requires Airmore application
 > to be open on every action (or depends on how you use). You can change
 > target device's locking behavior on settings, which will make this method
 > as pain-free as possible.
