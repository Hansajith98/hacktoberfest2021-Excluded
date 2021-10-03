import java.util.*;
  
public class AbstractListDemo {
    public static void main(String args[])
    {
  
        // Creating an empty AbstractList
        AbstractList<String>
            list = new LinkedList<String>();
  
        // Using add() method
        // to add elements in the list
        list.add("GFG");
        list.add("for");
        list.add("Geeks");
        list.add("computer");
        list.add("portal");
  
        // Output the list
        System.out.println("Original List: "
                           + list);
  
        // subList and clear method
        // to remove elements
        // specified in the range
        list.subList(1, 3).clear();
  
        // Print the final list
        System.out.println("Final List: "
                           + list);
    }
}
