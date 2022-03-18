# PyAcpTrak

## What is it?

**PyAcpTrak** helps you to create ACOPOStrak resources for training, meetings, mappView widgets, etc...

[![PyPI Latest Release](https://img.shields.io/pypi/v/PyAcpTrak)](https://pypi.org/project/PyAcpTrak/)
[![PyPI License](https://img.shields.io/pypi/l/PyAcpTrak)](https://github.com/HeytalePazguato/PyAcpTrak/blob/master/LICENSE)
[Python versions](https://img.shields.io/pypi/pyversions/PyAcpTrak)
[Twitter](https://img.shields.io/twitter/follow/HeytalePazguato?style=social)


## Install
```
pip install PyAcpTrak
```

## Main Features

### Work with segments

The library support 4 type of segments ('AA', 'AB', 'BA' and 'BB')

For each segment is possible to obtain the it's information and a svg image

```
from PyAcpTrak import *

segment('aa').info

segment('aa').plot(45)
```

## License

Copyright © Jorge Centeno

Laravel Livewire is open-sourced software licensed under the [MIT license](LICENSE.md).