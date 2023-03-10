from Node import  Node
from Btree import Btree
import sys



class Application :
    
    
    def main(args):

        """ root = Node()
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        n6 = Node()
        n7 = Node()
        n8 = Node()
        n9 = Node()
        n10 = Node()
        n11 = Node()
        n12 = Node()
        n13 = Node()
        n14 = Node()
        n15 = Node()
        n16 = Node()
        n17 = Node()
        n18 = Node()
        n19 = Node()
        n20 = Node()

        root.keys = [14]
        n1.keys = [6,10]
        n2.keys = [22,30]
        n3.keys = [4]
        n4.keys = [8]
        n5.keys = [12]
        n6.keys = [18]
        n7.keys = [26]
        n8.keys = [34]
        n9.keys = [2]
        n10.keys = [5]
        n11.keys = [7]
        n12.keys = [9]
        n13.keys = [11]
        n14.keys = [13]
        n15.keys = [16]
        n16.keys = [20]
        n17.keys = [24]
        n18.keys = [28]
        n19.keys = [32]
        n20.keys = [36]

        root.childs = [n1,n2]
        n1.childs = [n3,n4,n5]
        n2.childs = [n6,n7,n8]
        n3.childs = [n9,n10]
        n4.childs = [n11,n12]
        n5.childs = [n13,n14]
        n6.childs = [n15,n16]
        n7.childs = [n17,n18]
        n8.childs = [n19,n20]

        root.leaf = False
        n1.leaf = False
        n2.leaf = False
        n3.leaf = False
        n4.leaf = False
        n5.leaf = False
        n6.leaf = False
        n7.leaf = False
        n8.leaf = False  """
        

        root = Node()
        k=3
        tree = Btree(root,k)
        """ tree.insertion(12)
        tree.insertion(10)
        tree.insertion(13)
        tree.insertion(20)
        tree.insertion(4) 
        tree.insertion(5) 
        tree.insertion(35) 
        tree.insertion(34)  """
        for i in range(20):
            tree.insertion(i)
        """tree.insertion(1) 
        print(tree.root.keys)
        print(tree.root.childs[0].keys)
        print(tree.root.childs[1].keys) """
        print(tree.ptint_graphvoz())
        
        """ print()
        print("***** EXPLORER UN ARBRE *****")
        print("resultat d'explorer l'arbre : " , tree.explore())
        print()
        print("***** RECHERCHER UNE VALEUR DANS L'ARBRE *****")
        print(" rechercher la valuer 16 : ", tree.rechechre(16))
        print(" rechercher la valeur 2 : ", tree.rechechre(2))
        print(" rechercher la valeur 3 : ", tree.rechechre(3))
        print(" rechercher la valeur 36 : ", tree.rechechre(36))
        print(" rechercher la valeur 40 : ", tree.rechechre(40))
        print()
        print("***** HAUTEUR *****")
        print("la heuteur : " ,tree.hauteur())
        print()
        print("***** ARBRE ÉQUILIBRÉ *****")
        print(tree.balanced())
        print()
        print("***** ISBTREE? *****")
        print(tree.isBtree()) 
             """
            
    if __name__=="__main__" : 
        main(sys.argv)
        
    


        
        


