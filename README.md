GPIOInterrupts
==============
The Interrupts block monitors a GPIO pin for interrupts.

Properties
----------
- **pin**: The GPIO BCM pin to monitor for interrupts.
- **pull_up_down**: Value of `pin` when it's logic level is neither high nor low.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: At an interupt, the 'pin' is added to the signal.

Commands
--------
None

Dependencies
------------
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

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
The Read block reads from a variety of gpio interfaces. A 'pin' read is triggered by any incoming signal.

Properties
----------
- **pin**: The GPIO BCM pin to read.
- **pull_up_down**: Value of `pin` when it's logic level is neither high nor low.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Each input signal triggers a pin read. The boolean `pin` value is added to the signal.

Commands
--------
None

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
The Write block emits a signal containing a boolean value to a specified GPIO pin.

Properties
----------
- **pin**: The GPIO BCM pin to write.
- **value**: Boolean value to write to `pin`.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Each input signal triggers a pin write. The boolean `pin` value is added to the signal.

Commands
--------
None

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

