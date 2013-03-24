collective.js.extjs
===================

This package integrates the `Ext JS 3`_ library into Plone.

It provides:

- a resource directory (``++resource++collective.js.extjs-resources/``)
- a jquery adapter resource (``++resource++ext-jquery-adapter.js``)
- a generic setup profile, registering JavaScript and CSS to the portal registry.

It includes `Ext JS Library 3.4.0 <http://docs.sencha.com/ext-js/3-4/>`_.


Usage
=====

- Install the package by adding it to your buildout configuration:

::

    [instance]
    eggs =+
        collective.js.extjs

- Install the generic setup profile.


Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.1`, `4.2`.


Links
=====

- Ext JS 3.4 website: http://www.sencha.com/products/extjs3/
- Ext JS 3.4 documentation: http://docs.sencha.com/ext-js/3-4/
- Ext JS 3.4 licensing: http://www.sencha.com/products/extjs3/license/
- collective.js.extjs repository: https://github.com/4teamwork/collective.js.extjs
- collective.js.extjs tracker: https://github.com/4teamwork/collective.js.extjs/issues
- collective.js.extjs on pypi: http://pypi.python.org/pypi/collective.js.extjs


License
=======

The Ext JS 3.4 library is licensed under GPL3 amongst other licenses.
See the `Ext JS 3.4 license page`_ for further details.

`collective.js.extjs` is licensed under **GPL3**. When using this package the
license terms at the `Ext JS 3.4 license page`_ needs to be followed.


.. _Ext JS 3: http://www.sencha.com/products/extjs3/
.. _Ext JS 3.4 license page: http://www.sencha.com/products/extjs3/license/
