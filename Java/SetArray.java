import java.util.*;

public class SetArray {

    public static void main(String[] args) {

        Set<String> set = new HashSet<>();
        set.add("a");
        set.add("b");
        set.add("c");

        String[] array = new String[set.size()];
        set.toArray(array);

        System.out.println("Array: " + Arrays.toString(array));

    }
}
