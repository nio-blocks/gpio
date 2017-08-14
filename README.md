GPIOInterrupts
==============
Read and write on a variety of gpio interfaces.

Properties
----------
- **pin**: The pin to monitor for interrupts
- **pull_up_down**: Value of `pin` when it's logic level is neither high nor low.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Each input signal triggers an interrupt. The `pin` is added to the signal.

Commands
--------

Output Example
--------------
```
{
  'input_attr': 'I was already here',
  'pin': 'pin_property'
}
```


GPIORead
========

Properties
----------
- **pin**: The pin to read from.
- **pull_up_down**: Value of `pin` when it's logic level is neither high nor low.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Each input signal triggers a pin read. The boolean `pin` value is added to the signal.

Commands
--------

Dependencies
------------
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

Input
-----
Any list of signals.

Output Example
--------------
```
{
  'input_attr': 'I was already here',
  'value': True
}
```


GPIOWrite
=========

Properties
----------
- **pin**: The pin to write to.
- **value**: Bool value to write to `pin`.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Each input signal triggers a pin write. The boolean `pin` value is added to the signal.

Commands
--------

Dependencies
------------
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

Input
-----
Any list of signals.

Output Example
--------------
```
{
  'input_attr': 'I was already here',
  'value': 'value_property'
}
```
