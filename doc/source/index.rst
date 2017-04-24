.. lxml documentation master file, created by
   sphinx-quickstart on Sun Apr  2 16:30:39 2017.




lxml - XML and HTML with Python
===============================

| `“lxml takes all the pain out of XML.” <http://thread.gmane.org/gmane.comp.python.lxml.devel/3252/focus=3258>`_
| Stephan Richter
|

**lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.**


Introduction
------------

The lxml XML toolkit is a Pythonic binding for the C libraries
`libxml2`_ and `libxslt`_.  It is unique in that it combines the speed and
XML feature completeness of these libraries with the simplicity of a
native Python API, mostly compatible but superior to the well-known
**ElementTree** API.  The latest release works with all CPython versions
from 2.6 to 3.6.  See the `introduction`_ for more information about
background and goals of the lxml project.  Some common questions are
answered in the `FAQ`_.

.. _libxml2: http://xmlsoft.org/
.. _libxslt: http://xmlsoft.org/XSLT/
.. _introduction: intro.html
.. _FAQ:          FAQ.html


Support the project
-------------------

lxml has been downloaded from the **Python Package Index** more than two million times and is also available directly in many package distributions, e.g. for Linux or MacOS-X.

Most people who use lxml do so because they like using it. You can show us that you like it by blogging about your experience with it and linking to the project website.

If you are using lxml for your work and feel like giving a bit of your own benefit back to support the project, consider sending us money through PayPal that we can use for fixing bugs in the software and improving its features and documentation. Please read the Legal Notice below, at the bottom of this page. Thank you for your support.

.. container:: donate-button-container

  .. container:: donate-button

    `Donate <https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=R56JE3VCPDA9N>`_


Please **contact Stefan Behnel** for other ways to support the lxml project, as well as commercial consulting, customisations and trainings on lxml and fast Python XML processing.

.. _Donate: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=R56JE3VCPDA9N


Download
--------

The best way to download lxml is to visit `lxml at the Python Package
Index <http://pypi.python.org/pypi/lxml/>`_ (PyPI).  It has the source
that compiles on various platforms.  The source distribution is signed
with `this key`_.

.. _this key: pubkey.asc

The latest version is 3.7.2, released 2017-01-08,
**('changes for 3.7.2'_)**.  'Older versions <#old-versions>'_
are listed below.


Please take a look at the
`installation instructions <installation.html>`_ !

This complete web site (including the generated API documentation) is
part of the source distribution, so if you want to download the
documentation for offline use, take the source archive and copy the
``doc/html`` directory out of the source tree, or use the
'PDF documentation'_.

The latest installable developer sources should usually be available from the
`build server <http://lxml.de/build/>`_.  It's also possible to check out
the latest development version of lxml from github directly, using a command
like this (assuming you use hg and have hg-git installed)::

  hg clone git+ssh://git@github.com/lxml/lxml.git lxml

Alternatively, if you use git, this should work as well::

  git clone https://github.com/lxml/lxml.git lxml

You can browse the `source repository`_ and its history through
the web.  Please read `how to build lxml from source <build.html>`_
first.  The `latest CHANGES`_ of the developer version are also
accessible.  You can check there if a bug you found has been fixed
or a feature you want has been implemented in the latest trunk version.

.. _`source repository`: https://github.com/lxml/lxml/
.. _`latest CHANGES`: https://github.com/lxml/lxml/blob/master/CHANGES.txt


Mailing list
------------

Questions? Suggestions? Code to contribute? We have a `mailing list`_.

You can search the archive with Gmane_ or Google_.

.. _`mailing list`: http://lxml.de/mailinglist/
.. _Gmane: http://blog.gmane.org/gmane.comp.python.lxml.devel
.. _Google: http://www.google.com/webhp?q=site:comments.gmane.org%2Fgmane.comp.python.lxml.devel+


Bug tracker
-----------

lxml uses the `launchpad bug tracker`_.  If you are sure you found a
bug in lxml, please file a bug report there.  If you are not sure
whether some unexpected behaviour of lxml is a bug or not, please
check the documentation and ask on the `mailing list`_ first.  Do not
forget to search the archive (e.g. with Gmane_)!

.. _`launchpad bug tracker`: https://launchpad.net/lxml/


License
-------

The lxml library is shipped under a `BSD license`_. libxml2 and libxslt2
itself are shipped under the `MIT license`_. There should therefore be no
obstacle to using lxml in your codebase.

.. _`BSD license`: https://github.com/lxml/lxml/blob/master/doc/licenses/BSD.txt
.. _`MIT license`: http://www.opensource.org/licenses/mit-license.html


Legal Notice for Donations
--------------------------

Any donation that you make to the lxml project is voluntary and
is not a fee for any services, goods, or advantages.  By making
a donation to the lxml project, you acknowledge that we have the
right to use the money you donate in any lawful way and for any
lawful purpose we see fit and we are not obligated to disclose
the way and purpose to any party unless required by applicable
law.  Although lxml is free software, to the best of our knowledge
the lxml project does not have any tax exempt status.  The lxml
project is neither a registered non-profit corporation nor a
registered charity in any country.  Your donation may or may not
be tax-deductible; please consult your tax advisor in this matter.
We will not publish or disclose your name and/or e-mail address
without your consent, unless required by applicable law.  Your
donation is non-refundable.


old versions
------------

see the websites of lxml
`1.3 <http://lxml.de/1.3/>`_,
`2.0 <http://lxml.de/2.0/>`_,
`2.1 <http://lxml.de/2.1/>`_,
`2.2 <http://lxml.de/2.2/>`_,
`2.3 <http://lxml.de/2.3/>`_,
`3.0 <http://lxml.de/3.0/>`_,
`3.1 <http://lxml.de/3.1/>`_,
`3.2 <http://lxml.de/3.2/>`_,
`3.3 <http://lxml.de/3.3/>`_,
`3.4 <http://lxml.de/3.4/>`_,
`3.5 <http://lxml.de/3.5/>`_,
`3.6 <http://lxml.de/3.6/>`_

..
   and the `latest in-development version <http://lxml.de/dev/>`_.

.. _`pdf documentation`: lxmldoc-3.7.2.pdf

* `lxml 3.7.2`_, released 2017-01-08 (`changes for 3.7.2`_)

* `lxml 3.7.1`_, released 2016-12-22 (`changes for 3.7.1`_)

* `lxml 3.7.0`_, released 2016-12-10 (`changes for 3.7.0`_)

* `lxml 3.6.4`_, released 2016-08-18 (`changes for 3.6.4`_)

* `lxml 3.6.3`_, released 2016-08-18 (`changes for 3.6.3`_)

* `lxml 3.6.2`_, released 2016-08-18 (`changes for 3.6.2`_)

* `lxml 3.6.1`_, released 2016-07-24 (`changes for 3.6.1`_)

* `lxml 3.6.0`_, released 2016-03-17 (`changes for 3.6.0`_)

* `older releases <http://lxml.de/3.6/#old-versions>`_

.. _`lxml 3.7.2`: changes.html#id1
.. _`lxml 3.7.1`: changes.html#id2
.. _`lxml 3.7.0`: changes.html#id3
.. _`lxml 3.6.4`: changes.html#id4
.. _`lxml 3.6.3`: changes.html#id5
.. _`lxml 3.6.2`: changes.html#id6
.. _`lxml 3.6.1`: changes.html#id7
.. _`lxml 3.6.0`: changes.html#id8

.. _`changes for 3.7.2`: changes.html#id1
.. _`changes for 3.7.1`: changes.html#id2
.. _`changes for 3.7.0`: changes.html#id3
.. _`changes for 3.6.4`: changes.html#id4
.. _`changes for 3.6.3`: changes.html#id5
.. _`changes for 3.6.2`: changes.html#id6
.. _`changes for 3.6.1`: changes.html#id7
.. _`changes for 3.6.0`: changes.html#id8


Sitemap
-------

`Sitemap`_

.. _Sitemap: sitemap.html
