import java.util.*;

class Books {
	public String title;
	public String author;
	public int isbn;
	public double price;
	public double discount;
	public double total;

	public Books() {
	}

	public Books(String title, String author, int isbn, double price,
			double discount, double total) {
		super();
		this.title = title;
		this.author = author;
		this.isbn = isbn;
		this.price = price;
		this.discount = discount;
		this.total = total;
	}

	public String getTitle() {
		return title;
	}

	public String getAuthor() {
		return author;
	}

	public int getIsbn() {
		return isbn;
	}

	public double getPrice() {
		return price;
	}

	public double getDiscount() {
		return discount;
	}

	public double getTotal() {
		return total;
	}
}

public class BookStore {
	public static void main(String[] args) throws Exception {
		double amount = 0.0;
		double sum = 0.0;
		int count = 1;
		List list = new ArrayList();
		Scanner scan = new Scanner(System.in);
		int menu = 0;
		System.out.println("Book Store");
		System.out.println();
		System.out.println("1. Buy book");
		System.out.println("2. Receipt");
		System.out.println("3. Receive Payment");
		System.out.println("4. Exit");
		boolean quit = false;
		do {
			if (count > 5) {
				System.out
						.println("You cannot buy more than 5 books at a time.");
			}
		System.out.print("Please enter your choice: ");
		menu = scan.nextInt();
		System.out.println();
		switch (menu) {
		case 1:
		count++;
		System.out.println("Book Title: ");
		String booktitle = scan.next();
		System.out.println("Author: ");
		String auth = scan.next();
		System.out.println("ISBN: ");
		int no = scan.nextInt();
		System.out.println("Price: ");
		double p = scan.nextDouble();
		System.out.println("Discount: ");
	        double dis = scan.nextDouble();
		double total = p - (dis * p);
		list.add(new Books(booktitle,auth, no, p,dis, total)); 
                break;
		case 2:
		System.out.println("Title Author ISBN Price 
                Discount Total");
	        for (Books s : list) {
		System.out.println(s.getTitle() + " " + s.getAuthor()  
                + " "	+ s.getIsbn() + " "+ s.getPrice() + " "+ 
                s.getDiscount() + " " +	s.getTotal());
		sum += s.getTotal();
				}
			System.out.println("Total= " + sum);
			break;
			case 3:
			System.out.println("Customer Pays: ");
			amount = scan.nextDouble();
			double balance = amount - sum;
			System.out.println("Balance is: " + balance);
			quit = true;
			case 4:
			quit = true;
			break;
			default:
			System.out.println("Invalid Entry!");
			}
		} while (!quit);
	}
}
