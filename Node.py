class Node :
    
    def __init__(self) :
        self.keys = list() # les differentes valeur dans un seul noeud
        self.childs = list() # les fils d'un noued
        self.parent = None
        self.leaf = True

    
    def searchNode(self,key) : 
        """
            Rechercher une clé dans un noeud 
            Paramètres : 
            - key : int la clé qu'on veut rechercher dans un noeud 
            Valeur de retour : 
            - boolean True si la cle se trouve dans le noeud sinon renvoyer False     
            Contraintes :
            Exemples :
            >>>  tree.hauteur()
            3
           
        """ 
        i=0
        found = False
        while (i < self.keys.length() and (not found) ) :
            if (self.keys[i] == key ) :
                return True 
            i+=1
        return found

        
    
    def isLeaf(self) : 
        """
            Verifier si le noeud est une feuille 
            Paramètres :  
            Valeur de retour : 
            - boolean True si le noeud est une feuille sinon renvoyer False      
            Contraintes :
            Exemples :
            >>>  
           
        """ 
        return self.leaf


    def setLeaf(self) : 
        if (self.leaf == False) :
            self.leaf = True
        else : 
            self.leaf = False


    def getParent(self) : 
        return self.parent
    

    def setParent(self,newParent) : 
        self.parent = newParent
         

    def getChilds(self) :
        return self.childs


        