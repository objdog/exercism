class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []
        #I suspect a Python ninja could somehow work the 
        #below into the above variable declaration, but I'm 
        #new so I'll do it the long way.
        
        stringRows = matrix_string.split("\n") 
        
        #breaking the rows down into their subordinate values, 
        #turning them into integers and loading them into the self.rows.
        for row in stringRows: 
            scratchRow = row.split(" ")
            scratchRow = list(map(lambda i: int(i), scratchRow))
            self.rows.append(scratchRow)
       
        #This seems like a really awkward way to do this, 
        #but nesting a for loop to construct the columns by index.
        for i in range(0, len(self.rows[0])): 
            scratchCol = []
            for x in range(0, len(self.rows)):
                scratchCol.append(self.rows[x][i])
            
            self.columns.append(scratchCol)
            
    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]
