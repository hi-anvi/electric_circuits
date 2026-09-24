
class Battery:

    def __init__ (self, v=-1, i=-1):
        self.voltage = v
        self.current = i
        self.positiveT = None
        self.negativeT = None
    
    def __str__ (self):
        """Represents it in ASCII"""
        return f"{str(self.positionT)} <- |+| BATTERY \n{len(str(self.positiveT))*" "}Voltage = {self.voltage}V, Current = {self.current}A |-| -> {str(self.negativeT)}"

    def __eq__ (self, other):
        v = self.voltage == other.voltage
        c = self.current == other.current
        t = str(self.postiveT) == str(other.postiveT) and str(self.negativeT) == str(other.negativeT)
        return v and c and t


class Wire:

    def __init__ (self, end1=[], end2=[]):
        self.ends = [end1, end2]

    def __str__ (self):
        return "WIRE"

    def __eq__ (self, other):
        a = str(self.ends[0]) == str(other.ends[0]) and str(self.ends[1]) == str(other.ends[1])
        b = str(self.ends[1]) == str(other.ends[0]) and str(self.ends[1]) == str(other.ends[0])
        return a or b


class Resistor:

    def __init__ (self, r=-1, end1=[], end2=[], v=-1, i=-1):
        self.resistance = r
        self.voltage = v
        self.current = i
        self.ends = [end1, end2]

    def __str__ (self):
        return f"RESISTOR\nResistance = {self.resistance}Ω, Voltage = {self.voltage}V, Current =  {self.current}A"

    def __eq__ (self, other):
        v = self.voltage == other.voltage
        c = self.current == other.current
        r = self.resistance == other.resistance
        a = str(self.ends[0]) == str(other.ends[0]) and str(self.ends[1]) == str(other.ends[1])
        b = str(self.ends[1]) == str(other.ends[0]) and str(self.ends[1]) == str(other.ends[0])
        return v and c and r and (a or b)

    def findResistance (self, v, i): 
        if v < 0 or i <= 0: return None
        self.resistance = v / i
        return self.resistance

    def findVoltage (self, i, r):
        if i < 0 or r < 0: return None
        self.voltage = i * r
        return self.voltage
    
    def findCurrent (self, v, r):
        if v < 0 or r <= 0: return None
        self.current = v / r
        return self.current

    def update (self, v=None, i=None, r=None):

        if v is None: v = self.voltage
        if r is None: r = self.resistance
        if i is None: i = self.current

        a = self.findCurrent(v, r)
        b = self.findResistance(v, i)
        c = self.findVoltage(i, r)

        if (a is not None or b is not None or c is not None): return True
        else: return False
    