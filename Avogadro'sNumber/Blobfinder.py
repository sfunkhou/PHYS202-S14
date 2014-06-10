
class Blob(object):
    
    def __init__(self):
        """An empty blob
        """
        self.name = []
        self.mass = 0
    
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
        self.distance = ((blob2.com[0] - blob1.com[0])**2 + (blob2.com[1] - blob1.com[1])**2)**(0.5)
        return self.distance
    
    def centerOfMass(self):
        """returns tuple of (x,y) values for this bead's center of mass
        """
        x_i = 0
        y_i = 0
        for i in range(len(self.name)):
            x_i += self.name[i][0]
            y_i += self.name[i][1]
        x_c = x_i/self.mass
        y_c = y_i/self.mass
        self.com = (x_c,y_c)
        return self.com
    
def monochrome(picture,threshold):
    """looks at each pixel of the picture passed to it, and
    colors it black if greater than luminance threshold,
    white if not; employs fillrec below"""
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
        
def BlobFinder(picture, threshold): #monochrome
    """Returns an array of pixel tuples at which contiguous blobs
    satisfying the threshold are contingous. Calls monochrome, 
    count, and fill.
    """
    float(threshold)
    blob_list = []
    #xsize, ysize = picture.size
    monochrome(picture,threshold)
    blobs = count(picture,fill,blob_list)
    return blobs

def fillrec(picture, xsize, ysize, x, y):
    """Fastest means of coloration of blobs into "red",
    (from Counting Stars). Each call to 'fillrec' 
    takes care of one pixel, then calls 'fillrec'
    again to take care of the neighbors
    """
     
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    if picture[x,y] != BLACK:
        return
    picture[x,y] = (255,0,0)
    blob = Blob("name")
    blob.add(x,y)
    if x > 0:
        fillrec(picture, xsize, ysize, x-1, y)
    if x < (xsize-1):
        fillrec(picture, xsize, ysize, x+1, y)
    if y > 0:
        fillrec(picture, xsize, ysize, x, y-1)
    if y < (ysize-1):
        fillrec(picture, xsize, ysize, x, y+1)



def fill(picture, xsize, ysize, xstart, ystart, blob_current):
    """keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list"""
    queue = [(xstart,ystart)]
        
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = (255,0,0)
            blob_current.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    #return blob_current
                
    
def count(picture,fillfunc, blob_list):
    """scan the image top to bottom and left to right
    using a nested loop. When black pixel is found,
    increment the count, then call the fill function
    to fill in all the pixels connected to that one."""
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == (0,0,0):
                result += 1
                #new blob introduced:
                blobb = Blob()
                
                #appending list of contiguous blobbs
                fillfunc(temp,xsize,ysize,x,y, blobb)
                blobb.get_mass()
                blobb.centerOfMass()
                blob_list.append(blobb)
    return blob_list
          
def countBeads(P, blob_list):
    """returns number of beads with >= P pixels
    """
    n = 0
    for b in blob_list:
        if b.mass >= P:
            n += 1
    return n
        
def getBeads(P,blob_list):
    """returns all beads with >= P pixels
    """
    Blobs = []
    for b in blob_list:
        if b.get_mass >= P:
            Blobs.append(b)
    return Blobs

    

