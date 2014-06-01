class Blob(object):
    def _init_(self, name):
        self.name = []
    
    def add(self,i,j):
        self.name.append((i,j))
        
    def get_mass(self):
        self.mass = len(self.name)
    def distanceTo(self,blob1,blob2):
        self.distance = np.sqrt((centerOfMass(blob2)[0] - centerOfMass(blob1)[0])**2 + (centerOfMass(blob2)[0] - centerOfMass(blob1)[0])**2)
    def centerOfMass(self):
        x_i = 0
        for i in range(len(self.mass)):
            x_i += self[i][0]
            y_i += y[i][0]
        x_c = x_i/mass(self.mass)
        y_c = y_i/mass(self.mass)
        blob.com = (x_c,y_c)
    
def BlobFinder(picture, threshold): #monochrome
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= threshold: 
                    temp[x,y] = black
            else:
                    temp[x,y] = white
    
def fillrec(picture, tau):
    if picture[x,y] != BLACK:
        return
    picture[x,y] = RED
    blob.add(x,y)
    if x > 0:
        fillrec(picture, xsize, ysize, x-1, y)
    if x < (xsize-1):
        fillrec(picture, xsize, ysize, x+1, y)
    if y > 0:
        fillrec(picture, xsize, ysize, x, y-1)
    if y < (ysize-1):
        fillrec(picture, xsize, ysize, x, y+1)
    
def count(picture,fillfunc):
    """scan the image top to bottom and left to right
    using a nested loop. When black pixel is found,
    increment the count, then call the fill function
    to fill in all the pixels connected to that one."""
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                result += 1
                fillfunc(temp,xsize,ysize,x,y)
    return result
        
def countBeads(P, self):
    n = 0
    if self.mass() >= P:
        n += 1 
        
def getBeads(P, blob):
    for i in range(len(blob)):
        if blob.mass() != P:
            del blob.mass()[i]


