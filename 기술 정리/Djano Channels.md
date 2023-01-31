https://channels.readthedocs.io/en/latest/



# Django Channels

Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called [ASGI](https://asgi.readthedocs.io/).

Channels builds upon the native ASGI support in Django. Whilst Django still handles traditional HTTP, Channels gives you the choice to handle other connections in either a synchronous or asynchronous style.

To get started understanding Channels, read our [Introduction](https://channels.readthedocs.io/en/latest/introduction.html), which will walk through how things work.

Note

This is documentation for the **4.x series** of Channels. If you are looking for documentation for older versions, you can select `3.x`, `2.x`, or `1.x` from the versions selector in the bottom-left corner.

## Projects

Channels is comprised of several packages:

- [Channels](https://github.com/django/channels/), the Django integration layer
- [Daphne](https://github.com/django/daphne/), the HTTP and Websocket termination server
- [asgiref](https://github.com/django/asgiref/), the base ASGI library
- [channels_redis](https://github.com/django/channels_redis/), the Redis channel layer backend (optional)

This documentation covers the system as a whole; individual release notes and instructions can be found in the individual repositories.