GPIO
====

Read and write on a variety of gpio interfaces.

Dependencies
-----------
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

GPIORead
========

Read the value of a gpio pin.

Properties
----------
- **pin** (int): pin to read from
- **pull_up_down**: value of `pin` when it's logic level is neither high nor low

Dependencies
------------
None

Commands
--------
None

Input
-------
Any list of signals.

Output
------

Each input signal triggers a pin read. The boolean `pin` value is added to the signal.

```
{
  'input_attr': 'I was already here',
  'value': True
}
```

GPIOWrite
========

Write to the specified gpio pin.

Properties
----------
- **pin** (int): pin to write to
- **value** (bool): bool value to write to `pin`

Dependencies
------------
None

Commands
--------
None

Input
------
Any list of signals.

Output
------

Each input signal triggers a pin write. The boolean `pin` value is added to the signal.

```
{
  'input_attr': 'I was already here',
  'value': 'value_property'
}
```

GPIOInterrupt
==============
Notify an interrupt signal when the specified `pin` changes it's `value`.

Properties
----------
- **pin** (int): the pin to monitor for interrupts
- **pull_up_down**: value of `pin` when it's logic level is neither high nor low

Dependencies
------------
None

Commands
---------
None

Input
-------
Any list of signals.

Output
--------

Each input signal triggers an interrupt. The `pin` is added to the signal.

```
{
  'input_attr': 'I was already here',
  'pin': 'pin_property'
}
```
