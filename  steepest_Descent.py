# read each term, then add linear terms to a list, also a list for 2nd digree terms

import sys


class Term(object):
    def __init__(self):
        pass

    coefficient = 0
    dimension = 'x1'
    power = 1
    

    def set_term(self, coe, dim, pow):
        self.coefficient = coe
        self.dimension = dim
        self.power = pow
        pass

    def display_term(self):
        print(self.coefficient,self.dimension,end="")
        if self.dimension == 'x1x2':
            print('')
            return
        else:
            print('^', self.power)
    
    def get_dimension(self):
        return self.dimension
    
    def check_digree(self):
        return self.power





def main():
    coe = int(input("Enter coefficient of the term, enter 0 to finish: "))
    if coe == 0:
        sys.exit()
    dim = str(input("Enter the dimension for the term, note that only 2 dimensions (x1, x2) are acceptable for now: "))
    linear_terms = []
    quadratic_terms = []
    # add line to skikp the power if  the dim is x1x2
    if dim == 'x1' or dim =='x2':
        pow = int(input("Enter the power 'digree' of the term, note that only 1st and 2nd digree are acceptable for now: "))
    elif dim == 'x1x2':
        pow = 2
    
    t1 = Term()
    print("=================================")
    print(coe)
    print(dim)
    print(pow)
    t1.set_term(coe, dim, pow)
    if t1.check_digree() == 1:
        linear_terms.append(t1)
    elif t1.check_digree() == 2 or t1.get_dimension() == 'x1x2':
        quadratic_terms.append(t1)
    else:
        print("Digree is not acceptable")

    #print("Linear terms are:", linear_terms, len(linear_terms))
    print("Linear Terms are:")
    for i in linear_terms:
        i.display_term()
    #print("Quadratic terms are: ", quadratic_terms, len(quadratic_terms))

    print("Quadratic terms are:")
    for i in quadratic_terms:
        i.display_term()
    print('done')


main()