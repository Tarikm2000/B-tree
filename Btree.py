import Node 



class Btree : 
 

    def __init__(self,root,k) : 
        self.k = k 
        self.root = root

    

    def explore(self) :
        
        """
        Explorer l'arbre 
        Valeur de retour : 
        - liste de tous les noeuds de l'arbre apres l'exploration de ce dernier  
        Contraintes :
        Exemples :
        >>> explore(tree) tree etant l'arbre du cours
        [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]   
        """
        
        res = []
        if (self.root.isLeaf()) : 
            for i in range (len(self.root.keys)) : 
                res.append(self.root.keys[i])
        else :
            
            l = self.root.childs
            tree = Btree(l[0],self.k)
            res = tree.explore()
            for i in range (len(self.root.keys)):
                res.append(self.root.keys[i])
                tree1 = Btree(l[i+1],self.k)
                res = res+ tree1.explore()
        return res

    
    
    
    
    def rechechre(self,value) :
        """
        Rechecrhcer une valeur dans un arbre 

        Paramètres : la valeur qu'on veut voir si elle est dans l'arbre
        Valeur de retour : 
        - boolean True si la valeur existe dans l'arbre sinon renvoie False   
        Contraintes :
        - value doit etre un entier 
        Exemples :
        >>>  tree.rechechre(16)
        True
        >>> tree.recherche(3)
        False
        
        """
        if (value in self.root.keys):
            return True
        elif (self.root.isLeaf()):
            return False
        else:
            i = 0
            while (i < len(self.root.keys) and value > self.root.keys[i]):
                i += 1
            tree =  Btree(self.root.childs[i],self.k)
            return tree.rechechre(value)


    def hauteur(self) :
        """
            Calculer la hauteur d'un arbre 
            Paramètres : 
            Valeur de retour : 
            - int designant la hauteur de l'arbre    
            Contraintes :
            Exemples :
            >>>  tree.hauteur()
            3
           
        """ 
        if (self.root.isLeaf()) : 
            return 0
        else : 
            l =[]
            for child in self.root.childs : 
                tree = Btree(child,self.k)
                l.append(tree.hauteur())
            return max(l) + 1


    def balanced(self) : 
        """
            Verefier que l'arbre est équilibré
            Paramètres : 
            Valeur de retour : 
            - True si l'arbre est equilibre sinon renvoyer False 
            Contraintes :
            Exemples :
            >>>  tree.balanced()
            True 
           
        """ 
        if (self.root.isLeaf()) : 
            return True
        else : 
            l =[]
            for child in self.root.childs :
                tree=Btree(child,self.k)
                l.append(tree.hauteur())
            i=0
            while i < len(l)-1:
                if l[i]!=l[i+1]:
                    return False 
                i+=2 
            bools =[]
            for child in self.root.childs :
                tmp=Btree(child,self.k)
                bools.append(tmp.balanced())
            return all(bools)  #return true only if all the boolans of the list are True otherwise return False 
