import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Arrays;

public class IntervalTree {

  static ArrayList<int[]> closedIntervalList = new ArrayList<int[]>(); 
  Node root; //rót trésins

  //FG: Lokuðu bilin eru geymd í tré sem hefur rót í root. 
  //Öll bil sem prenta skal út eru geymd í closedIntervalList
  
  public IntervalTree() 
  {
    root = null;
  }
  
  //Notkun: tree.insert(a,b);
  //Fyrir: a og b eru heiltölur, a < b
  //Eftir: búið er að bæta bilinu [a,b] í tréð
  public void insert(int a, int b)
  {
    if(b < a) return;
    
    Node newNode = new Node();
    newNode.lower = a;
    newNode.higher = b;
    newNode.insertInterval(a,b);
    
    if(root == null) {
      root = newNode;
      return;
    }
    
    Node tree = root;
    
    while(tree != null)
    {
      if(b < tree.lower)
      {
        if(tree.left != null)
        {
          tree = tree.left;
        }
        else
        {
          newNode.parent = tree;
          tree.left = newNode;
          return;
        }
      }
      else if(a > tree.higher)
      {
        if(tree.right != null)
        {
          tree = tree.right;
        }
        else
        {
          newNode.parent = tree;
          tree.right = newNode;
          return;
        }
      }
      else
      {
        tree.insertInterval(a,b);
        return;
      }
    }
  }
  
  //Notkun: tree.delete(a,b);
  //Fyrir: a og b eru heiltölur, a <= b
  //Eftir: Ef [a,b] var í trénu þá er búið að eyða því
  public void delete(int a, int b)
  {       
    if(root == null || b < a) return;
    
    Node tree = root;
    
    while(tree != null)
    {
      if(b < tree.lower)
      {
        if(tree.left != null)
        {
          tree = tree.left;
        }
        else
        {
          return;
        }
      }
      else if(a > tree.higher)
      {
        if(tree.right != null)
        {
          tree = tree.right;
        }
        else
        {
          return;
        }
      }
      else
      {
        tree.deleteInterval(a,b);
        if(tree.intervals == null)
        {
          deleteNode(tree);
        }
        return;
      }
    }
  }

  //Notkun: tree.intersects(a,b,root);
  //Fyrir: a og b eru heiltölur, a < b, root er nóða
  //Eftir: búið er að finna öll bil sem skerast á við [a,b]
  public int intersects(int a, int b, Node node)
  {
    if(b < a) return 0;
    
  
    if(node == null)
    {
      return 0;
    }
    
    int instanceFound = 0;
    
    Node tree = node;
    
    if(a < tree.lower)
    {
      instanceFound = instanceFound + intersects(a,b, tree.left);
    }
    
    instanceFound = instanceFound + node.findIntersections(a,b);
    
    if(b > tree.higher)
    {
      instanceFound = instanceFound + intersects(a,b, tree.right);
    }
    return instanceFound;
  }
  
  //Notkun: tree.intersects(a,b,root);
  //Fyrir: a og b eru heiltölur, a < b, root er nóða
  //Eftir: búið er að finna og prenta öll bil sem skerast á við [a,b]
  public void intersects(int a, int b)
  {
    int instance = intersects(a, b, root);
    if(instance == 0)
    {
      System.out.print("[]");
    }else{
      printFoundIntervals();
    }
    System.out.println("");
  }
  
  //Notkun: tree.contains(a,b,root);
  //Fyrir: a og b eru heiltölur, a <= b, root er nóða
  //Eftir: búið er að finna öll bil sem innihalda[a,b]
  public boolean contains(int a, int b, Node node)
  {
    if(b < a) return false;
  
    if(node == null)
    {
      return false;
    }
    
    boolean instanceFound = false;
    
    Node tree = node;
    
    if(a < tree.lower)
    {
      boolean left =  contains(a,b, tree.left);
      instanceFound = instanceFound || left;
    }
    
    boolean center = tree.findContains(a,b);
    instanceFound = instanceFound || center;
    
    if(b > tree.higher)
    {
      boolean right = contains(a,b, tree.right);
      instanceFound = instanceFound || right;
    }       

    return instanceFound;
  }

  //Notkun: tree.contains(a,b);
  //Fyrir: a og b eru heiltölur, a <= b, root er nóða
  //Eftir: búið er að finna og prenta öll bil sem innihalda[a,b]
  public void contains(int a, int b)
  {
    boolean instance = contains(a, b, root);
    if(!instance)
    {
      System.out.print("[]");
    }else{
      printFoundIntervals();
    }
    System.out.println("");
  }
  
  //Notkun: tree.point(a);
  //Fyrir: a er heiltala
  //Eftir: búið er að finna og prenta öll bil sem innihalda a
  public void point(int a)
  {
    boolean instance = contains(a, a, root);
    if(!instance)
    {
      System.out.print("[]");
    }else{
      printFoundIntervals();
    }
    System.out.println("");
  }
  
  //Notkun: printFoundIntervals()
  //Fyrir:  Ekkert
  //Eftir:  Búið er að prenta öll þau bil sem leitað var að
  public void printFoundIntervals(){

    // Comparator sem sér um að röðun
    Comparator<int[]> sort = new Comparator<int[]>() {
      public int compare(int[] a, int[] b) {
        if(a[0] < b[0])         return -1;
        else if(a[0] > b[0])    return 1;
        else                    return 0;
      }
    };

    Collections.sort(closedIntervalList, sort);

    for (int[] arr : closedIntervalList) {
      System.out.print(Arrays.toString(arr)+" ");
    }
    closedIntervalList.clear();
  }   
  
  //Notkun: tree.deleteNode(node)
  //Fyrir: node er nóða
  //Eftir: Búið er að fjarlægja node úr trénu
  public void deleteNode(Node node)
  {
    
    if(node == null) return;
  
    if(node.left == null && node.right == null)
    {
      node = null;
      return;
    }
    if(node.right == null)
    {
      node.left.parent = node.parent;
      node = node.left;
      return;
    }
    
    Node search = node.right;
    while(search.left != null)
    {
      search = search.left;
    }
    
    Node copyOfSearch = search;
    
    search = search.right;
    copyOfSearch.parent = node.parent;
    node = copyOfSearch;
  }
  
  //Notkun: tree.query(q);
  //Fyrir: q er strengur sem inniheldur fyrirspurn í Interval tréð
  //Eftir: Búið er að framkvæma fyrirspurnina í q.
  public void query(String query) {
    String[] splitQuery = query.split(" ");
    int lower = Integer.parseInt(splitQuery[1]);
    
    if(splitQuery[0].equals("?p"))
    {
      point(lower);
    }
    else 
    {               

      int higher = Integer.parseInt(splitQuery[2]);
      
      if(splitQuery[0].contains("+"))
      {
        insert(lower, higher);
      }
      else if(splitQuery[0].equals("-"))
      {
        delete(lower, higher);
      }   
      else if(splitQuery[0].equals("?o"))
      {
        intersects(lower,higher);
      }
      else if(splitQuery[0].equals("?i"))
      {
        contains(lower,higher);
      }                       
    }               
  
  }

  //nóðurnar í trénu
  static class Node 
  {
    int lower; //neðri mörk
    int higher; //efri mörk
    Node left; //vinstra barn
    Node right; //hægra barn
    Node parent; //foreldri
    Link intervals; //bilin sem skerast á við bilið í nóðunni
    
    //FG: Lokuðu bilin í nóðunni eru geymd í tengda listanum intervals, hægra barn
    //nóðurnar er í right og vinstra barn í left. Foreldri nóðunnar er parent. 
    //lower er lægri endi fyrsta lokaða bilsins sem var sett í nóðuna og higher 
    //er hærri endi lokaðs bilsins. 
    
    static class Link 
    {
      Link next;
      int lower;
      int higher;
      
      //FG: next bendir á næsta hlekk í tengda listanum, lower er lægri endi lokaðs bils
      // og higher er hærri endi lokaðs bils.
      
      //Notkun: link.compareTo(a,b);
      //Fyrir: a og b eru heiltölur, a < b
      //Eftir: Skilar 1 ef [lower,higher] < [a,b], 0 ef þau eru jöfn og -1 annars
      int compareTo(int a, int b)
      {
        if(lower < a)
        {
          return 1;
        }
        else if(lower > a)
        {
          return -1;
        }
        else
        {
          if(higher < b)
          {
            return 1;
          }
          else if(higher > b)
          {
            return -1;
          }
          else
          {
            return 0;
          }
        }
      }
    }
    
    //Notkun: node.insertInterval(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að setja bilið [a,b] á réttan stað í intervals
    void insertInterval(int a, int b)
    {
      Link newLink = new Link();
      newLink.lower = a;
      newLink.higher = b;
      if( intervals == null || intervals.compareTo(a,b)<0 )
      {
        newLink.next=intervals;
        intervals=newLink;
        return;
      }
      if(intervals.lower == a && intervals.higher == b)
      {
        return;
      }
      Link temp = intervals;
      while( temp.next != null )
      {
        if( temp.next.compareTo(a,b) > 0 )
        {
          temp = temp.next;
        }
        else if( temp.next.compareTo(a,b) == 0 )
          return;
        else
        {
          newLink.next = temp.next;
          temp.next = newLink;
          return;
        }
      }
      newLink.next = temp.next;
      temp.next = newLink;
    }

    //Notkun: node.findIntersections(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að finna öll bil sem skerast á við bilið [a,b]
    int findIntersections(int a,int b)
    {
      Link chain = intervals;
      
      int found = 0;
      
      while(chain != null)
      {
        if(chain.lower > b) break;
      
        if((chain.lower <= b && chain.higher >= b) || (chain.lower <= a && chain.higher >= a))
        {
          int[] closedInterval = {chain.lower, chain.higher};
          closedIntervalList.add(closedInterval);
          found++;
        }
        else if((chain.lower >= a && chain.lower <= b) || (chain.higher >= a && chain.higher <= b))
        {
          int[] closedInterval = {chain.lower, chain.higher};
          closedIntervalList.add(closedInterval);
          found++;
        }
        
        chain = chain.next;
      }
      
      return found;
    }
    
    //Notkun: node.findContains(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að finna öll bil sem innihalda [a,b]
    boolean findContains(int a,int b)
    {
      Link chain = intervals;
      
      boolean found = false;

      while(chain != null)
      {
        if(chain.lower > a) break;
        
        if(chain.lower <= a && b <= chain.higher)
        {
          int[] closedInterval = {chain.lower, chain.higher};
          closedIntervalList.add(closedInterval);
          found = true;
        }
        chain = chain.next;
      }

      return found;
    }
    
    //Notkun: node.deleteInterval(a,b);
	//Fyrir: a og b eru heiltölur, a < b
	//Eftir: Búið er að fjarlægja lokaða bilið [a,b] ef það var geymt í nóðunni.
    void deleteInterval(int a, int b)
    {
      if(intervals == null) return;
      
      //athugar hvort fremsta stakið sé það sem verið er að leita af
      if(intervals.lower == a && intervals.higher == b)
      {
        intervals = intervals.next;
        return;
      }

      Link chain = intervals;
      
      //fer í gegnum afganginn af listanum og leitar
      while(chain.next != null)
      {
        if(chain.next.lower == a && chain.next.higher == b)
        {
          chain.next = chain.next.next;
          return;
        }
        
        chain = chain.next;
      }
    }
    
  }
    
  public static void main(String[] args)
  {
    IntervalTree tree = new IntervalTree();
    Scanner scanner = new Scanner(System.in);
    while(scanner.hasNext())
    {
      String query = scanner.nextLine();
      tree.query(query);
    }
  }
}
      
      
      
      