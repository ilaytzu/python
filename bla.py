array = [[' ', ' ', ' ', 'x', ' ', ' ', ' '],
         ['x', ' ', ' ', 'x', 'x', ' ', ' '],
         [' ', ' ', ' ', ' ', 'x', 'x', ' '],
         [' ', ' ', ' ', ' ', 'x', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', 'x', 'x', 'x', 'x', ' ', ' '],
         ['x', ' ', ' ', 'x', ' ', ' ', ' ']]

def ex46(array,x,y)
    if( array[x][y] == ' ')
        return 0
    else
        if( x==0)
            if( y==0)
                return 1 + ex46(array, x+1, y) + ex46(array, x, y+1)
            else if( y==6)
                return 1 + ex46(array, x+1, y) + ex46(array, x, y-1)
            else
                return 1 + ex46(array, x+1, y) + ex46(array, x, y-1) + ex46(array, x, y+1)
        else if( x==6)
            if( y==0)
                return 1 + ex46(array, x-1, y) + ex46(array, x, y+1)
            else if( y==6)
                return 1 + ex46(array, x-1, y) + ex46(array, x, y-1)
            else
                return 1 + ex46(array, x-1, y) + ex46(array, x, y-1) + ex46(array, x, y+1)
        else)
            if( y==0)
                return 1 + ex46(array, x+1, y) + ex46(array, x-1, y) + ex46(array, x, y+1)
            else if( y==6)
                return 1 + ex46(array, x+1, y) + ex46(array, x-1, y) + ex46(array, x, y-1)
            else
                return 1 + ex46(array, x+1, y) + ex46(array, x-1, y) + ex46(array, x, y-1) + ex46(array, x, y+1)


print(ex46(array,2,5))