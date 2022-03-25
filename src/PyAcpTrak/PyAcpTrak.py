import svgutils.compose as sc
import numpy as np
from IPython.display import display
from importlib import resources
from typing import Final, List, Dict, TypeVar, Type, Sequence
from typeguard import typechecked

TSegment = TypeVar("TSegment", bound="Segment")
TTrack = TypeVar("TTrack", bound="Track")
TAssembly = TypeVar("TAssembly", bound="Assembly")

def get_resource(module: str, name: str) -> str:
    return resources.files(module).joinpath(name)

#Segment class
@typechecked
class Segment(object):
    def __init__(self, s: str) -> None:
        self._s = s.lower()
        self._figure = None
        if (self._s == 'aa'):
            self._info = {
                'name': None,
                'length': 660,
                'type': '8F1I01.AA66.xxxx-1',
                'description': 'ACOPOStrak straight segment'
            }
            self._svg = 'segment_aa.svg'
            self._img = {'tl': (0.0, 0.25),
                            'bl': (0.0, 10.74),
                            'tr': (66.0, 0.25),
                            'br': (66.0, 10.74),
                            'w': 66.0,
                            'h': 10.074,
                            'rs': 0.0,
                            're': 0.0}
        elif (self._s == 'ab'):
            self._info = {
                'name': None,
                'length': 450,
                'type': '8F1I01.AB2B.xxxx-1',
                'description': 'ACOPOStrak curve segment A'
            }
            self._svg = 'segment_ab.svg'
            self._img = {'tl': (0.0, 0.25),
                            'bl': (0.0, 9.98),
                            'tr': (44.6, 3.56),
                            'br': (40.89, 12.523),
                            'w': 44.6,
                            'h': 12.523,
                            'rs': 0.0,
                            're': 22.5}
        elif (self._s == 'ba'):
            self._info = {
                'name': None,
                'length': 450,
                'type': '8F1I01.BA2B.xxxx-1',
                'description': 'ACOPOStrak curve segment B'
            }
            self._svg = 'segment_ba.svg'
            self._img = {'tl': (0.0, 3.56),
                            'bl': (3.71, 12.523),
                            'tr': (44.6, 0.25),
                            'br': (44.6, 9.98),
                            'w': 44.6,
                            'h': 12.523,
                            'rs': 22.5,
                            're': 0.0}
        elif (self._s == 'bb'):
            self._info = {
                'name': None,
                'length': 240,
                'type': '8F1I01.BB4B.xxxx-1',
                'description': 'ACOPOStrak circular arc segment'
            }
            self._svg = 'segment_bb.svg'
            self._img = {'tl': (0.0, 2.59),
                            'bl': (4.35, 13.081),
                            'tr': (23.2, 2.59),
                            'br': (18.85, 13.081),
                            'w': 23.2,
                            'h': 13.081,
                            'rs': 22.5,
                            're': 22.5}
        else:
            raise ValueError('Segment not supported. Supported segments "AA", "AB", "BA" or "BB"')
    
    def info(self) -> Dict[str, any]:
        return {k: v for k, v in self._info.items() if v is not None}

    def plot(self, angle: float = 0) -> TSegment:
        angle %= 360.0

        w = self._img['w']
        h = self._img['h']
        
        nw = (abs(w*np.cos(np.deg2rad(angle))) + abs(h*np.cos(np.deg2rad(90+angle)))).round(3)
        nh = (abs(w*np.sin(np.deg2rad(angle))) + abs(h*np.sin(np.deg2rad(90+angle)))).round(3)
        nx = (nw - ((w*np.cos(np.deg2rad(angle))) + (h*np.cos(np.deg2rad(90+angle)))).round(3))/2
        ny = (nh - ((w*np.sin(np.deg2rad(angle))) + (h*np.sin(np.deg2rad(90+angle)))).round(3))/2
        
        self._figure = sc.Figure(str(nw) + 'mm', str(nh) + 'mm', sc.SVG(get_resource('img', self._svg)).move(nx,ny).rotate(angle))
        
        display(self._figure)
        
        return self
    
    def save(self, name: str = 'Segment.svg') -> None:
        if not isinstance(name, str):
            raise TypeError('The "name" argument must be string')

        self._figure.save(name)
    
    def __add__(self, other: (TSegment|TTrack)) -> TTrack:
        if isinstance(other, Segment):
            return Track([self, other])
        elif isinstance(other, Track):
            new_track = [self]
            new_track += other.segment.copy()
            return Track(new_track)
        else:
            raise TypeError('Segments can only be added to  Segment or Track objects')
    
    def __mul__(self, other: int) -> TTrack:
        if isinstance(other, int):
            if other < 0:
                raise TypeError('Segments can only be multiplied by positive integers')
            l = list()
            for i in range(other):
                l.append(self.__class__(self._s))
            return Track(l)
        else:
            raise TypeError('Segments can only be multiplied by positive integers')
    
    __rmul__ = __mul__
    
#Track class
@typechecked
class Track(object):
    def __init__(self, segments: List[Segment], seg_prefix: str = 'gSeg_', seg_offset: int = 1):
        if seg_offset < 0:
            raise TypeError('The "seg_offset" argument must be a positive integer')

        self.segment = [Segment(seg._s) for seg in segments]
        self.seg_prefix = seg_prefix
        self.seg_offset = seg_offset
        
    def __add__(self, other: (TSegment|TTrack)) -> TTrack:
        new_track = self.segment.copy()
        if isinstance(other, Segment):
            new_track.append(other)
        elif isinstance(other, Track):
            other_track = self.__class__(other.segment, other.seg_prefix, other.seg_offset)
            new_track = new_track + other_track.segment
        else:
            raise TypeError('Tracks can only be added to Segment or Track objects')
        return Track(new_track)
    
    def __mul__(self, other: int) -> TTrack:
        if isinstance(other, int):
            if other < 0:
                raise TypeError('Tracks can only be multiplied by positive integers')
            new_track = self.segment.copy()
            new_track = new_track * other
            return Track(new_track)
        else:
            raise TypeError('Tracks can only be multiplied by positive integers')
    
    def __len__(self) -> int:
        return len(self.segment)
    
    def info(self) -> Dict[str, any]:
        for i, s in enumerate(self.segment):
            s._info['name'] = self.seg_prefix + str(i + self.seg_offset).zfill(3)
        return {
            'length': sum(s._info['length'] for s in self.segment),
            'segment': [s._info for s in self.segment],
        }
    
    def plot(self, angle: float = 0) -> TTrack:
        angle %= 360.0

        xabs = self.segment[0]._img['tl'][0]
        yabs = self.segment[0]._img['tl'][1]
        rot = angle
        gap = 0.5
        xmax = 0.0
        ymax = 0.0
        xmin = 0.0
        ymin = 0.0

        asm = []
        for seg in self.segment:
            rot += seg._img['rs']
            xabs += (seg._img['tl'][1] * np.sin(np.deg2rad(rot)))
            yabs -= (seg._img['tl'][1] * np.cos(np.deg2rad(rot)))
            
            w = seg._img['w']
            h = seg._img['h']
            nw = [(w*np.cos(np.deg2rad(rot))).round(3), (h*np.cos(np.deg2rad(90+rot))).round(3)]
            nh = [(w*np.sin(np.deg2rad(rot))).round(3), (h*np.sin(np.deg2rad(90+rot))).round(3)]
            
            xmax = max(xmax, xabs, xabs + sum(x for x in nw if x > 0))
            ymax = max(ymax, yabs, yabs + sum(y for y in nh if y > 0))
            xmin = min(xmin, xabs, xabs + sum(x for x in nw if x < 0))
            ymin = min(ymin, yabs, yabs + sum(y for y in nh if y < 0))
    
            asm.append(sc.SVG(get_resource('img', seg._svg)).move(round(xabs, 3), round(yabs, 3)).rotate(round(rot, 3)))
    
            xabs += ((seg._img['tr'][0] * np.cos(np.deg2rad(rot))) + (seg._img['tr'][1] * np.cos(np.deg2rad(rot + 90))) + (gap * np.cos(np.deg2rad(rot))))
            yabs += ((seg._img['tr'][0] * np.sin(np.deg2rad(rot))) + (seg._img['tr'][1] * np.sin(np.deg2rad(rot + 90))) + (gap * np.sin(np.deg2rad(rot))))
            rot +=  seg._img['re']
        
        nw = (abs(xmax) + abs(xmin))
        nh = (abs(ymax) + abs(ymin))
        nx = abs(xmin)
        ny = abs(ymin)
        
        self._figure = sc.Figure(str(nw) + 'mm', str(nh) + 'mm', *asm).move(nx, ny)

        display(self._figure)
        
        return self
    
    def save(self, name: str = 'Track.svg') -> None:
        self._figure.save(name)
    
    __rmul__ = __mul__
    
#Loop class
@typechecked
class Loop(Track):
    def __init__(self, l: int = 2, w: int = 1, **kwars) -> None:
        self._l = l
        self._w = w

        if (self._l < 2):
            raise ValueError('The length of the loop must be at least 2')
        elif (self._w < 1):
            raise ValueError('The width of the loop must be at least 1')
        else:
            if (self._w == 1):
                self._track = TRACK180 + ((self._l - 2) * TRACK0) + TRACK180 + ((self._l - 2) * TRACK0)
            else:
                self._track = TRACK90 + ((self._w - 2) * TRACK0) + TRACK90 + ((self._l - 2) * TRACK0) + TRACK90 + ((self._w - 2) * TRACK0) + TRACK90 + ((self._l - 2) * TRACK0)
        super().__init__(self._track.segment, **kwars)

    def __add__(self, other: (TSegment|TTrack)) -> TAssembly:
        if isinstance(other, Segment):
            new_track = Track([other])
            return Assembly([self, new_track])
        elif isinstance(other, Track):
            return Assembly([self, other])

    def __mul__(self, other: int) -> TAssembly:
        l = [self]
        return Assembly([ item for item in l for _ in range(other) ])

    __rmul__ = __mul__

    def save(self, name: str = 'Loop.svg') -> None:
        self._figure.save(name)

#Assembly class
@typechecked
class Assembly(object):
    def __init__(self, tracks: List[Track], name: str = 'gAssembly_1') -> None:
        self.name = name
        self.track = list()
        
        old_prefix = None
        for track in tracks:
            if old_prefix != track.seg_prefix:
                t_len = track.seg_offset
            self.track.append(Track(track.segment, track.seg_prefix, t_len))
            t_len += len(track)
            old_prefix = track.seg_prefix
    
    def info(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'length': sum(t.info()['length'] for t in self.track),
            'track': [t.info() for t in self.track],
        }

class _sh_param:
    def __init__(self):
        self.shuttle ={
                'count': '10',
                'convoy': 'Inactive',
                'collision_distance': '0.002',
                'error_stop': '0.006',
                'sh_stereotype': 'ShuttleStereotype_1',
                'sh_size': '50',
                'magnet_plate': '2',
                'magnet_type': 'Straight',
                'collision_strategy': 'Constant',
                'extent_front': '0.025',
                'extent_back': '0.025',
                'width': '0.046',
            }

PARAM: Final = _sh_param()

#Get shuttle model
def get_sh_model(param = PARAM.shuttle):
    if (param['sh_size'] == '50'):
        print('bien', param['sh_size'])
    else:
        raise ValueError('The input dictionary must include the key "sh_size"')

    if ('magnet_plate' in param):
        print('bien')
    else:
        raise ValueError('The input dictionary must include the key "magnet_plate"')

    if ('magnet_type' in param):
        print('bien')
    else:
        raise ValueError('The input dictionary must include the key "magnet_type"')

#Constant definition
TRACK0: Final = Track([Segment('aa')])
TRACK45: Final = Track([Segment('ab'), Segment('ba')])
TRACK90: Final = Track([Segment('ab'), Segment('bb'), Segment('ba')])
TRACK135: Final = Track([Segment('ab'), Segment('bb'), Segment('bb'), Segment('ba')])
TRACK180: Final = Track([Segment('ab'), Segment('bb'), Segment('bb'), Segment('bb'), Segment('ba')])

