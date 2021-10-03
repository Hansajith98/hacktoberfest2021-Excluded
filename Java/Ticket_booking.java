/* Driver Code:
import java.util.Scanner;
public class TicketBooking {
    public static void main(String[] args) {
        Scanner tk = new Scanner(System.in);
        int availTickets = tk.nextInt();
        int reqJohn = tk.nextInt();
        int reqMike = tk.nextInt();
        AvailableTicket avlTic = new AvailableTicket(availTickets,reqJohn,reqMike);
        Thread t = new Thread(avlTic);
        Thread tt = new Thread(avlTic);
        t.setName("John");
        tt.setName("Mike");
        t.setPriority(10);
        t.start();
        tt.start();
    }
}
*/

class AvailableTicket extends Thread{
  // Write your code here
    int available;
    int wantedMike;
    int wantedJohn;
    public AvailableTicket(int avail, int reqJohn, int reqMike) {
        available = avail;
        wantedMike = reqMike;
        wantedJohn = reqJohn;
    }
    public void run() {
        synchronized (this) {
            int wanted;
            String threadName = Thread.currentThread().getName();
            if(threadName=="John") {
                wanted = wantedJohn;
            }
            else {
                wanted = wantedMike;
            }
            if(available >= wanted) {
                System.out.print(Thread.currentThread().getName());
                System.out.println(": tickets booked: " + wanted);
                available = available - wanted;
            }
            else {
                System.out.println(Thread.currentThread().getName() + ": not booked");
            }
        }
    }
}
