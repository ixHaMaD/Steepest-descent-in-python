# read each term, then add linear terms to a list, also a list for 2nd digree terms
# add constant (k)

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
        '''if self.coefficient != 1 or self.coefficient != -1:
            print(self.coefficient,end="")
        if self.coefficient == -1:
            print('-',end='')'''

        
        print(self.coefficient, self.dimension,end="")
        if self.dimension == 'x1x2':
            print('')
            return
        else:
            print('^', self.power)
    
    def get_coefficient(self):
        return self.coefficient
    
    def get_dimension(self):
        return self.dimension
    
    def check_digree(self):
        return self.power





def main():
    linear_terms = []
    quadratic_terms = []

    while True:
        coe = int(input("Enter coefficient of the term, enter 0 to finish: "))
        if coe == 0:
            break
        dim = str(input("Enter the dimension for the term, note that only 2 dimensions (x1, x2) are acceptable for now: "))
       
        # check dimension
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
        #seperating terms as lienar terms and quad terms
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
        
    constant = int(input("Enter constant value: "))
    standard_form(linear_terms, quadratic_terms, constant)
    
  

def standard_form(linear_terms, quadratic_terms, constant):
    Q = [[],[]]
    c = [] 
    k = constant

    #seperate each dimension
    x1_quad = []
    x1_linear = []
    x2_quad = []
    x2_linear = []
    x1x2_quad = []
    for i in quadratic_terms:
        if i.get_dimension() == 'x1':
            x1_quad.append(i)
        elif i.get_dimension() == 'x2':
            x2_quad.append(i)
        elif i.get_dimension() == 'x1x2':
            x1x2_quad.append(i)
            
    print('x1_quad')
    for i in x1_quad:
        i.display_term()
    
    print('x2_quad')
    for i in x2_quad:
        i.display_term()
    
    print('x1x2_quad')
    for i in x1x2_quad:
        i.display_term()
    
    for i in linear_terms:
        if i.get_dimension() == 'x1':
            x1_linear.append(i)
        elif i.get_dimension() == 'x2':
            x2_linear.append(i)
    
    print('x1_linear')
    for i in x1_linear:
        i.display_term()
    
    print('x2_linear')
    for i in x2_linear:
        i.display_term()
        
    
    x11 = x1_quad[0].get_coefficient() * 2
    x22 = x2_quad[0].get_coefficient() * 2 
    x12 = x1x2_quad[0].get_coefficient()
    Q = [[x11, x12],
         [x12,x22]]
    
    #print the Hessian (Q)
    print('==============Hessian=============')
    print("Q =\t",end='')
    for i in Q:
        print('\t')
        for j in i:
            print(j,end='\t')
        print()
    print('===============================')

    detQ = (x11*x22) - (x12*x12)

    print('det(Q) = ', detQ)
    if detQ > 0:
        print("Function is convex")

    


main()