class Modem(object):
  def Dial(pno):
    return pno
  def Hangup():
    return
  def Send(c):
    return c
  def Recv():
    return 0
  def Accept(self, visitor):
    return


class HayesModem(Modem):
  configurationString = None;
  def Accept(self, visitor):
    visitor.Visit(self)

class ZoomModem(Modem):
  configurationValue = 0;
  def Accept(self, visitor):
    visitor.Visit(self)

class ErnieModem(Modem):
  internalPattern = None;
  def Accept(self, visitor):
    visitor.Visit(self)


class UnixModemConfigurator(object):

  def Visit(self, modem):
    if (modem.__class__.__name__ == 'HayesModem'):
      modem.configurationString = "&s1=4&D=3"
    elif (modem.__class__.__name__ == 'ZoomModem'):
      modem.configurationValue = 42
    elif (modem.__class__.__name__ == 'ErnieModem'):
      modem.internalPattern = "C is too slow"



