from IPL2020 import venue as mv
from IPL2020.RCB import venue as bv
from IPL2020.KKR import venue as kv

mv.printStadium()
bv.printStadium()
kv.printStadium()

mv.printVenue()
bv.printVenue()
kv.printVenue()


from IPL2020.Venue import printStadium as ms
from IPL2020.KKR.venue import printStadium as kkrs
from IPL2020.RCB.venue import printStadium as rcbs


ms()
kkrs()
rcbs()