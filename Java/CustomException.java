import java.util.ArrayList;
import java.util.Arrays;

// create a checked exception class
class CustomException extends Exception {
  public CustomException(String message) {
    // call the constructor of Exception class
    super(message);
  }
}

class Main {

  ArrayList<String> languages = new ArrayList<>(Arrays.asList("Java", "Python", "JavaScript"));

  // check the exception condition
  public void checkLanguage(String language) throws CustomException {

    // throw exception if language already present in ArrayList
    if(languages.contains(language)) {
      throw new CustomException(language + " already exists");
    }
    else {
      // insert language to ArrayList
      languages.add(language);
      System.out.println(language + " is added to the ArrayList");
    }
  }

  public static void main(String[] args) {

    // create object of Main class
    Main obj = new Main();

    // exception is handled using try...catch
    try {
      obj.checkLanguage("Swift");
      obj.checkLanguage("Java");
    }

    catch(CustomException e) {
      System.out.println("[" + e + "] Exception Occured");
    }
  }
}
