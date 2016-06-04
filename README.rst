narcolepsy
==========

Sleep soundly. Sleep randomly.


Overview
--------
The ``narcolepsy`` package contains code which alters the behavior of your
application/api by injecting random sleep calls into its code paths.


Usage
-----
The following code is an example of using the ``@narcoleptic`` decorator.
::

    from narcolepsy import narcoleptic

    @narcoleptic(max=5)  # sleep for 5 seconds at max
    def foobar():
        for x in xrange(1024):
            nested_function(x)

Installation
------------
The easiest way to install ``narcolepsy`` is via ``pip``:
::
    $ pip install narcolepsy


Why?
----
Why not? There are probably testing applications that I haven't considered
where timing is an integral component to the execution environment. Or you
could use this to make sneaking by CAPTCHAs a bit easier :D


LICENSE
-------
See the LICENSE file for details.
