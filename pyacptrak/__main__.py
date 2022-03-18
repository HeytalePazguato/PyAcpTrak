#__main__.py

from PyAcpTrak import *

def main():
	TRACK0 = track([segment('aa')])
	TRACK45 = track([segment('ab'), segment('ba')])
	TRACK90 = track([segment('ab'), segment('bb'), segment('ba')])
	TRACK135 = track([segment('ab'), segment('bb'), segment('bb'), segment('ba')])
	TRACK180 = track([segment('ab'), segment('bb'), segment('bb'), segment('bb'), segment('ba')])

if __name__ == '__main__':
	main()