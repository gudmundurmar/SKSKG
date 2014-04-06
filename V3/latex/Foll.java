public class IntervalTree {

  static ArrayList<int[]> closedIntervalList = new ArrayList<int[]>(); 
  Node root; //rót trésins

  //FG: Lokuðu bilin eru geymd í tré sem hefur rót í root. 
  //Öll bil sem prenta skal út eru geymd í closedIntervalList
  
  public IntervalTree() { root = null;  }
  
  //Notkun: tree.insert(a,b);
  //Fyrir: a og b eru heiltölur, a < b
  //Eftir: búið er að bæta bilinu [a,b] í tréð
  public void insert(int a, int b){}
  
  //Notkun: tree.delete(a,b);
  //Fyrir: a og b eru heiltölur, a <= b
  //Eftir: Ef [a,b] var í trénu þá er búið að eyða því
  public void delete(int a, int b){}

  //Notkun: tree.intersects(a,b,root);
  //Fyrir: a og b eru heiltölur, a <= b, root er nóða
  //Eftir: búið er að finna öll bil sem skarast á við [a,b] í trénu með rótina root
  public int intersects(int a, int b, Node node){}
  
  //Notkun: tree.intersects(a,b);
  //Fyrir: a og b eru heiltölur, a <= b
  //Eftir: búið er að finna og prenta út öll bil sem skarast á við bilið [a,b]
  public void intersects(int a, int b) {}
  
  //Notkun: tree.contains(a,b,root);
  //Fyrir: a og b eru heiltölur, a <= b, root er nóða
  //Eftir: búið er að finna öll bil sem innihalda[a,b] í trénu með rótina root
  public boolean contains(int a, int b, Node node){}

  //Notkun: tree.contains(a,b);
  //Fyrir: a og b eru heiltölur, a <= b, root er nóða
  //Eftir: búið er að finna og prenta öll bil sem innihalda[a,b]
  public void contains(int a, int b){}
  
  //Notkun: tree.point(a);
  //Fyrir: a er heiltala
  //Eftir: búið er að finna og prenta öll bil sem innihalda a
  public void point(int a){}
  
  //Notkun: printFoundIntervals()
  //Fyrir:  Ekkert
  //Eftir:  Búið er að prenta öll þau bil sem leitað var að
  public void printFoundIntervals(){}   
  
  //Notkun: tree.deleteNode(node)
  //Fyrir: node er nóða
  //Eftir: Búið er að fjarlægja node úr trénu
  public void deleteNode(Node node){}
  
  //Notkun: tree.query(q);
  //Fyrir: q er strengur sem inniheldur fyrirspurn fyrir Interval tréð
  //Eftir: Búið er að framkvæma fyrirspurnina í q.
  public void query(String query) {}

  //nóðurnar í trénu
  static class Node 
  { /*Sjá næstu földunarhæð hér að neðan*/  }
    
  public static void main(String[] args)
  {
    //Býr til nýtt tré sem það síðan
    //byggir upp með inntaki sem lesið er inn af standard input
  }
}