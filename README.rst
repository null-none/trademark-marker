Class for use https://markerapi.com/


=======
Install
=======

.. code-block:: bash

    pip install trademac-trademark

=======
Example
=======

.. code-block:: python

  from trademark import marker

  params = {
          'username': 'TRADEMARK_USERNAME',
          'password': 'TRADEMARK_PASSWORD',
          'search': 'word'
        }
  trademark = marker.API(params)
  print trademark.result()


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
