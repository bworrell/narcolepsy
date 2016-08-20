narcolepsy
==========

Sleep soundly. Sleep randomly.

|pypi badge| |downloads badge|

.. |pypi badge| image:: https://img.shields.io/pypi/v/narcolepsy.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/narcolepsy/
.. |downloads badge| image:: https://img.shields.io/pypi/dm/narcolepsy.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/narcolepsy/

Overview
--------

The ``narcolepsy`` package contains code which alters the behavior of your
application/api by injecting random sleep calls into decorated functions.


Usage
-----

The following code is an example of using the ``@narcoleptic`` decorator.

::

    from narcolepsy import narcoleptic

    @narcoleptic(max=5)  # sleep for 5 seconds at max
    def foobar():
        for x in xrange(1024):
            nested_function(x)
            
The ``@narcoleptic`` decorator takes three parameters (all optional):

*  ``min``: The minimum sleep time in seconds.
*  ``max``: The maximum sleep time in seconds.
*  ``chance``: The maximum number of lines that will be executed before a ``sleep()`` 
   call is injected.

If no ``min`` or ``max`` are passed in, the constants defined in 
``narcolepsy.constants`` will be used instead.
If no ``chance`` is passed in, a value will be derived from the number of lines 
in the input function.

Installation
------------

The easiest way to install ``narcolepsy`` is via ``pip``:

::

    $ pip install narcolepsy


Known Issues
------------
As mentioned in the `official documentation`_, ``sys.settrace()`` isn't part
of the Python language definition and thus, may not be available to all
Python implementations.

.. _official documentation: https://docs.python.org/2/library/sys.html#sys.settrace


Why?
----

In theory this could help test time-critical code (multi-producer/consumer
concurrent applications), but I mostly just wanted to play around with line
tracers.


Disclaimer
----------

This is a proof of concept and probably shouldn't be used in any sort of
real-world scenario where testing of time-critical code has any measure of
importance. **USE AT YOUR OWN RISK!**


LICENSE
-------

See the LICENSE file for details.
