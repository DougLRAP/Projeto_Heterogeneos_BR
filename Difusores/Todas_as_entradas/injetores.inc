WELL  'INJE 1'
INJECTOR MOBWEIGHT 'INJE 1'
INCOMP  WATER
OPERATE  MAX  STW  0.5 CONT
OPERATE  MAX  BHP  1000  CONT
**               rad      geofac    wfrac   skin
*GEOMETRY  *J    1.125    0.37       1.00    0.0  
PERF        WI  'INJE 1'
** UBA             wi          Status  Connection  
  2 1 1           -  OPEN    FLOW-FROM  'SURFACE'
  3 1 1           -  OPEN    FLOW-FROM  1
  4 1 1           -  OPEN    FLOW-FROM  2
  1 1 2           -  OPEN    FLOW-FROM  3
  2 1 2           -  OPEN    FLOW-FROM  4
  3 1 2           -  OPEN    FLOW-FROM  5
  4 1 2           -  OPEN    FLOW-FROM  6
  5 1 2           -  OPEN    FLOW-FROM  7
  1 1 3           -  OPEN    FLOW-FROM  8
  2 1 3           -  OPEN    FLOW-FROM  9
  3 1 3           -  OPEN    FLOW-FROM  10
  4 1 3           -  OPEN    FLOW-FROM  11
  5 1 3           -  OPEN    FLOW-FROM  12
  1 1 4           -  OPEN    FLOW-FROM  13
  2 1 4           -  OPEN    FLOW-FROM  14
  3 1 4           -  OPEN    FLOW-FROM  15
  4 1 4           -  OPEN    FLOW-FROM  16
  5 1 4           -  OPEN    FLOW-FROM  17
  2 1 5           -  OPEN    FLOW-FROM  18
  3 1 5           -  OPEN    FLOW-FROM  19
  4 1 5           -  OPEN    FLOW-FROM  20







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
