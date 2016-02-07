import sys                                                                          
from itertools import combinations                                               
                                                                                 
def main(reader, writer):                                                        
    n, m = map(int, reader.next().split())                                       
    people = (int(reader.next().strip(), 2) for _ in xrange(n))                     
    comb = map(lambda x: bin(x[0] | x[1]), combinations(people, 2))              
                                                                                 
    counter, max1 = 0, 0                                                         
    for combi in comb:                                                           
        n1 = combi.count('1')                                                    
        if n1 > max1:                                                            
            max1, counter = n1, 1                                                                                                                                                                                  
        elif n1 == max1:                                                         
            counter += 1                                                         
                                                                                 
    print >> writer, max1                                                        
    print >> writer, counter                                                        
                                                                                 
if __name__ == '__main__':                                                       
    main(sys.stdin, sys.stdout) 
