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


    def listNodes(self):
        if (self.isLeaf):
            return '"'+str(self.keys)+'"'+'\n'
        else :
            res=""
            for child in self.childs:
                res+='"'+(str(self.keys))+'"'+"\n"
                res+=child.listNodes()
            return res
    

    def listArcs(self):
        if(self.isLeaf):
            return ""
        else :
            res=""
            for child in self.childs:
                res+=('"'+str(self.keys)+'"'+"->"+'"'+str(child.keys))+'"'+"\n"
                res+=child.listArcs()
            return res


    def indice(self,value,liste) :
        trouve = False
        fin = False
        index = 0
        while (index<len(liste) and not trouve and not fin) : 
            if (liste[index] == value) : 
                trouve = True
            elif (value<liste[index]) : 
                break
            index+=1
        return (trouve,index)


    def split_child(self,position,k):
        new_node = Node()
        node_to_split = self.childs[position]
        self.childs.insert(position+1,new_node)
        
        res=self.indice(node_to_split.keys[k//2],self.keys)
        self.keys.insert(res[1],node_to_split.keys[k//2])
        new_node.keys=node_to_split.keys[k//2+1:]
        node_to_split.keys=node_to_split.keys[0:k//2]

        if  (not node_to_split.isLeaf):
            new_node.childs=node_to_split.childs[k//2+1:]
            node_to_split.childs=node_to_split.childs[:k//2+1]




