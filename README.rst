
=======
 Jthon
=======
This is a utility to make working with JSON files easier.

Installation 
=============

pip install jthon

Usage
------

.. code-block:: python

    import jthon
    a_new_dict = {
        'fruits': {
            'pineapple':0,
            'apples': 2,
            'orange': 4,
            'pears': 1
        }
    }
    example = jthon.load('fruits', a_new_dict)
    find = example.find(key='apple', exact=False)
    for found in find:
        print("I've found '{}', with a value of '{}'.".format(found.key, found.value))
        print("{}".format(found.siblings))

    print("There are {} oranges in the dict!".format(example.get('fruits').get('orange')))
    example['fruits']['peach'] = 1
    example.save()
    print(example)

More examples can be found in the examples folder

Requirements
-------------

.. code::
    
    python3.6 >




Authors
=======
* **CasuallyCalm** - `GitHub <https://github.com/CasuallyCalm>`__
* **ProbsJustin** - `GitHub <https://github.com/SobieskiCodes>`__

.. _ProbsJustin:


License
========

This project is licensed under MIT - see the [LICENSE](LICENSE.txt) file for details