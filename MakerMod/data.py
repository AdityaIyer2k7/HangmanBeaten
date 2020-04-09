class xy:
  def __init__(self,label="None",x=0,y=0,z=0):
    self.label=label
    self.x=x
    self.y=y
    self.z=z
    defX=x
    defY=y
    defZ=z
  def transpose(self,dx=0,dy=0,dz=0,magnitude=1,xSide=1,ySide=1,zSide=1):
    self.x=self.x+(dx*magnitude*xSide)
    self.y=self.y+(dy*magnitude*ySide)
    self.z=self.z+(dz*magnitude*zSide)
  def dataOut(self):
    return {"label":self.label,"x":self.x,"y":self.y,"z":self.z}
  def select(self,var="label"):
    allVar=self.dataOut()
    return [allVar.get(var)]
  def reset(self):
    self.label="None"
    self.x=self.defX
    self.y=self.defY
    self.z=self.defZ
  def set(self,x,y,z,rx,ry,rz):
    self.x=x
    self.y=y
    self.z=z

class graph:
  def __init__(self,coordinates=[xy()],yIsMag=True,xDiff=1,yDiff=1):
    self.coordinates=coordinates
    self.yIsMag=yIsMag
    self.xDiff=xDiff
    self.yDiff=yDiff
    self.mag=[]
    for coord in coordinates:
      if yIsMag == True:
        self.mag.append(coord.y*yDiff)
      else:
        self.mag.append(coord.x*xDiff)
    Dat=[]
    for c in coordinates:
      Dat.append([c.x*xDiff,c.y*yDiff])
    self.Dat=Dat
  def addPoint(self,point):
    coordinates.append(point)
    Dat.append(point)
    self.Dat=Dat
  def mags(self):
    return self.mag
  def data(self):
    return self.Dat
