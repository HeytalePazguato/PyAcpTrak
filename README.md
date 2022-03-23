# pyacptrak

## What is it? THIS

**pyacptrak** helps you to create ACOPOStrak resources for projects, training, meetings, mappView widgets, etc...

[![PyPI Latest Release](https://img.shields.io/pypi/v/pyacptrak)](https://pypi.org/project/pyacptrak/)
[![PyPI License](https://img.shields.io/pypi/l/pyacptrak)](https://github.com/HeytalePazguato/pyacptrak/blob/master/LICENSE)
![Python versions](https://img.shields.io/pypi/pyversions/pyacptrak)
[![Twitter](https://img.shields.io/twitter/follow/HeytalePazguato?style=social)](https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fpublish.twitter.com%2F&ref_src=twsrc%5Etfw%7Ctwcamp%5Ebuttonembed%7Ctwterm%5Efollow%7Ctwgr%5EHeytalePazguato&region=follow_link&screen_name=HeytalePazguato)


## Install
```
pip install pyacptrak
```

## Main Features

### Work with segments

The library support the 4 type of segments ('AA', 'AB', 'BA' and 'BB')

Obtain segment information:

```
from pyacptrak import *

print(Segment('aa').info)
```

Output:
```
{'length': 660,
 'type': '8F1I01.AA66.xxxx-1',
 'description': 'ACOPOStrak straight segment'}
```
Plot segment:
```
from pyacptrak import *

Segment('aa').plot()
```
![image](https://user-images.githubusercontent.com/101816677/158948767-9d10a414-21d3-42b3-ab1c-e54eace0c39f.png)

<pyacptrak.pyacptrak.segment at 0x17d8f72d930>


The plot function supports rotation in degrees
```
from pyacptrak import *

Segment('ab').plot(-45)
```
![image](https://user-images.githubusercontent.com/101816677/158949082-e38760c1-25fe-425e-b56e-ef96c223fbc2.png)

<pyacptrak.pyacptrak.segment at 0x17daed042b0>

### Work with tracks

The library has 5 types of pre-built tracks (TRACK0, TRACK45, TRACK90, TRACK135 and TRACK180)

```
from pyacptrak import *

TRACK135.plot()
```
![image](https://user-images.githubusercontent.com/101816677/158949482-f06e91bc-f8b9-4e11-b0fc-a7fe1149a15e.png)

<pyacptrak.pyacptrak.track at 0x17daec2f250>

But you could also build your own tracks using individual segments

```
from pyacptrak import *
track1 = (Segment('aa') * 2) + Segment('ab') + (Segment('bb') * 2) + Segment('ba')
track1.plot()
```
![image](https://user-images.githubusercontent.com/101816677/158949973-eea998ae-32fc-491f-955c-c5fbef496978.png)

<pyacptrak.pyacptrak.track at 0x17daf060700>

Or using the pre-configured tracks

```
from pyacptrak import *
track1 = (TRACK0 * 2) + TRACK135
track1.plot()
```
![image](https://user-images.githubusercontent.com/101816677/158949973-eea998ae-32fc-491f-955c-c5fbef496978.png)

<pyacptrak.pyacptrak.track at 0x17daf060700>

The plot function supports rotation for tracks

```
from pyacptrak import *
track1 = (TRACK0 * 2) + TRACK135
track1.plot(15)
```
![image](https://user-images.githubusercontent.com/101816677/158950300-9ffa4009-c5fe-4402-8284-003a8c8d5a1f.png)

<pyacptrak.pyacptrak.track at 0x17daef17f10>

### Work with loops

The library supports working with loops, the arguments for the loop are width and height, the unit is considering the 660mm grid so a `loop(2,1)` would draw the smallest possible loop

```
from pyacptrak import *
Loop(2,1).plot()
```
![image](https://user-images.githubusercontent.com/101816677/158950730-1c74eb26-49b6-483a-b807-2f9887d9b7d8.png)

<pyacptrak.pyacptrak.track at 0x17daed040a0>

For loops wider than 1 it uses 90° tracks instead of 180°

```
from pyacptrak import *
Loop(3,2).plot()
```
![image](https://user-images.githubusercontent.com/101816677/158950937-3a69abb0-5b25-4b3a-9b56-447b6b741304.png)

<pyacptrak.pyacptrak.track at 0x17daf0b8880>

The plot function also support rotation for loops

```
from pyacptrak import *
Loop(3,2).plot(190)
```
![image](https://user-images.githubusercontent.com/101816677/158951085-4ce1008d-aa84-4158-98d0-e83406bb5326.png)

<pyacptrak.pyacptrak.track at 0x17daf0ce020>

## License

Copyright © Jorge Centeno

pyacptrak is open-sourced software licensed under the [MIT license](LICENSE).
