# Nameof project= Merak
# made by Sahar Nikkhah
#This is to find the time lag of Merak light to reach the telescopes relative to each other/and this code use the formula in MerakTimeLag note. 
from subprocess import call
from astropy.coordinates import EarthLocation
from astropy.time import Time
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
from datetime import datetime, timedelta
import math
#===============finding time lag formula is from slides==========
def Time_lag(T1X,T1Y,T1H,T2X,T2Y,T2H,az,alt):
    theta12=math.atan((T1X-T2X)/(T1Y-T2Y))
    beta12=math.acos(math.sqrt((math.pow((T1X-T2X),2))+(math.pow((T1Y-T2Y),2)))/math.sqrt((math.pow((T1X-T2X),2))+(math.pow((T1Y-T2Y),2))+(math.pow((T1H-T2H),2))))
    alpha12=math.acos(math.cos(az-theta12)*math.cos(alt))
    delta12=math.sqrt((math.pow((T1X-T2X),2))+(math.pow((T1Y-T2Y),2))+(math.pow((T1H-T2H),2)))
    t= delta12*math.cos(alpha12+beta12)/3e8
    return t


#==================some infos====================
observing_time = Time('2021-03-31 3:00:00')# observing starts
observing_time2= Time('2021-03-31 3:00:07')#observing ends
Merak= SkyCoord.from_name('Merak')#finding Merak in sky
Veritas= EarthLocation(lat='31.675', lon='-110.952')#loaction of orgin in slides

#============telescopes locations(slides)========
T1X=135.48
T1Y=-8.61
T1H= 12.23
T2X=44.1
T2Y=-47.7
T2H=4.4
T3X=29.4
T3Y=60.1
T3H=9.8
T4X=-35.9
T4Y=11.3
T4H= 7.0

 #======start of loop over time============
while observing_time < observing_time2:
    #taking star data for the time
    aa = AltAz(location=Veritas, obstime=observing_time) 
    altdeg=Merak.transform_to(aa).alt.deg
    azdeg=Merak.transform_to(aa).az.deg
    alt= math.radians(altdeg)
    az=math.radians(azdeg)
    
     
    #time lag
  
    print('=================',observing_time,'===================')
    t12=Time_lag(T1X,T1Y,T1H,T2X,T2Y,T2H,az,alt)
    t13=Time_lag(T1X,T1Y,T1H,T3X,T3Y,T3H,az,alt)
    t14=Time_lag(T1X,T1Y,T1H,T4X,T4Y,T4H,az,alt)
    t23=Time_lag(T2X,T2Y,T2H,T3X,T3Y,T3H,az,alt)
    t24=Time_lag(T2X,T2Y,T2H,T4X,T4Y,T4H,az,alt)
    t34=Time_lag(T3X,T3Y,T3H,T4X,T4Y,T4H,az,alt)
	

    print('t12=',t12,'\n','t13=',t13, '\n','t14=',t14, '\n','t24=',t24, '\n','t23=',t23, '\n','t34=',t34 )
    
    observing_time += timedelta(0,1)
