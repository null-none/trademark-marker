Class for use https://markerapi.com/


=======
Install
=======

.. code-block:: bash

    pip install trademark-marker

=======
Example
=======

.. code-block:: python

  from trademark.marker import API

  params = {
    'username': 'username',
    'password': 'password',
    'search': 'search'
  }

  marker = API(params)

  print marker.result()


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
