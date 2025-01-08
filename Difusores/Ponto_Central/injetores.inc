WELL  'INJE 1'
INJECTOR MOBWEIGHT 'INJE 1'
INCOMP  WATER
OPERATE  MAX  STW  .5 CONT
OPERATE  MAX  BHP  1000  CONT
**               rad      geofac    wfrac   skin
*GEOMETRY  *J    1.125    0.37       1.00    0.0  
PERF        WI  'INJE 1'
** UBA             wi          Status  Connection  
2 1 2           -  OPEN    FLOW-FROM  'SURFACE'


  *TIME 600.0
DTWELL 0.00166667
  *ALTER 'INJE 1'
  0.5

  *TIME 1200.0
DTWELL 0.00166667
  *ALTER 'INJE 1'
  0.5

  *TIME 2160.0
DTWELL 0.00166667
  *ALTER 'INJE 1'
  0.5

  *TIME 3600.0
DTWELL 0.00166667
  *ALTER 'INJE 1'
  0.5

  *TIME 5040.0
DTWELL 0.00166667
  *ALTER 'INJE 1'
  0.5

  *TIME 7920.0
