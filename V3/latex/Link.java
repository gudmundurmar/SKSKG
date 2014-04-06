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
      int compareTo(int a, int b){}
    }