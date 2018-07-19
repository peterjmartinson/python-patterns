from visitor import *

v = UnixModemConfigurator()
h = HayesModem()
z = ZoomModem()
e = ErnieModem()

def test_HayesForUnix():
  h.Accept(v);
  assert  "&s1=4&D=3" == h.configurationString

def test_ZoomForUnix():
  z.Accept(v);
  assert  42 == z.configurationValue

def test_HayesForUnix():
  e.Accept(v);
  assert  "C is too slow" == e.internalPattern


