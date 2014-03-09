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
    	//Sjá næstu földun í skjalinu
    }
    
    //Notkun: node.insertInterval(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að setja bilið [a,b] á réttan stað í intervals
    void insertInterval(int a, int b){}

    //Notkun: node.findIntersections(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að finna öll bil sem skerast á við bilið [a,b]
    int findIntersections(int a,int b){}
    
    //Notkun: node.findContains(a,b);
    //Fyrir: a og b eru heiltölur, a < b
    //Eftir: búið er að finna öll bil sem innihalda [a,b]
    boolean findContains(int a,int b){}
    
    //Notkun: node.deleteInterval(a,b);
	//Fyrir: a og b eru heiltölur, a < b
	//Eftir: Búið er að fjarlægja lokaða bilið [a,b] ef það var geymt í nóðunni.
    void deleteInterval(int a, int b){}
    
  }