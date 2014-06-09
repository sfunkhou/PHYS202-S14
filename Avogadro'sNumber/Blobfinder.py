
class Blob(object):
    
    def __init__(self, name):
        """An empty blob
        """
        self.name = []
    
    def add(self,i,j):
        """add a pixel to a blob
        """
        self.name.append((i,j))
        
    def get_mass(self):
        """return mass as number of pixels added
        """
        self.mass = len(self.name)
        
    def distanceTo(self,blob1,blob2):
        """returns distance between the centers of masses of blob1 and blob2
        """
        self.distance = np.sqrt((blob2[0] - centerOfMass(blob1)[0])**2 + (blob2[0] - centerOfMass(blob1)[0])**2)
    
    def centerOfMass(self):
        """returns tuple of (x,y) values for this bead's center of mass
        """
        x_i = 0
        y_i = 0
        for i in range(len(self.mass)):
            x_i += self[i][0]
            y_i += self[0][i]
        x_c = x_i/self.mass
        y_c = y_i/self.mass
        blob.com = (x_c,y_c)
    
def BlobFinder(self, picture, threshold): #monochrome
    """looks at each pixel of the picture passed to it, and
    colors it black if greater than luminance threshold,
    white if not; employs fillrec below
    """
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
    #x_start = 1
    #y_start = 1
#def fillrec(self, picture, xsize, ysize, xstart, ystart):
    """Fastest means of coloration of blobs into "red",
    (from Counting Stars). Each call to 'fillrec' 
    takes care of one pixel, then calls 'fillrec'
    again to take care of the neighbors
    """
     
    #instance of blob
    #blob = Blob()
    #self.add(x,y)
    
    queue = [(xstart,ystart)]
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            self.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    
    
        
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
          
def countBeads(P):
    """returns number of beads with >= P pixels
    """
    n = 0
    if self.mass() >= P:
        n += 1 
        
def getBeads(self, P):
    """returns all beads with >= P pixels
    """
    for i in range(len(self.name)):
        if self.mass[i] != P:
            del self.mass[i]


