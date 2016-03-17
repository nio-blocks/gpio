GPIO
====

Read and write on a variety of gpio interfaces.

GPIORead
========

Read the bool value of a gpio pin.

Properties
----------
- Pin (bool) - ping to read from.

Dependencies
------------
None

Commands
--------
None

Output
------

Each input signal triggers a pin read. The boolean `pin` value is added to the signal.

```
{
  'input_attr': 'I was already here',
  'value': True,
}
```
