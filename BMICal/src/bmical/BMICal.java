package bmical;

import java.awt.EventQueue;
import java.awt.Font;
import javax.swing.JComboBox;
import javax.swing.JRadioButton;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;
import java.awt.event.ActionEvent;
import javax.swing.JScrollPane;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class BMICal {

  private JFrame frame;
  private JTextField tF1;
  private JTextField tF2;
  private JComboBox cB1;
  private JComboBox cB2;
  private JComboBox cB3;
  String day,year,month;
  String he="",we="",gen="",res="";
  private ButtonGroup genGP;
  private String dates[]
           = { "1", "2", "3", "4", "5",
               "6", "7", "8", "9", "10",
               "11", "12", "13", "14", "15",
               "16", "17", "18", "19", "20",
               "21", "22", "23", "24", "25",
               "26", "27", "28", "29", "30",
               "31" };
       private String months[]
           = { "Jan", "feb", "Mar", "Apr",
               "May", "Jun", "July", "Aug",
               "Sup", "Oct", "Nov", "Dec" };
       private String years[]
           = { "1987", "1988", "1989", "1990",
             "1991", "1992", "1993", "1994",
             "1995", "1996", "1997", "1998",
               "1999", "2000", "2001", "2002",
               "2003", "2004", "2005", "2006",
               "2007", "2008", "2009", "2010",
               "2011", "2012", "2013", "2014",
               "2015", "2016", "2017", "2018",
               "2019","2020","2021" };

  /**
   * Launch the application.
   */
  public static void main(String[] args) {
    EventQueue.invokeLater(new Runnable() {
      public void run() {
        try {
          BMICal window = new BMICal();
          window.frame.setVisible(true);
        } catch (Exception e) {
          e.printStackTrace();
        }
      }
    });
  }

  /**
   * Create the application.
   */
  public BMICal() {
    initialize();
  }

  /**
   * Initialize the contents of the frame.
   */
  private void initialize() {
    frame = new JFrame();
    frame.setBounds(100, 100, 310, 310);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.getContentPane().setLayout(null);
    
    JLabel lblNewLabel = new JLabel("BMI CALCULATOR");
    lblNewLabel.setBounds(86, 12, 142, 33);
    frame.getContentPane().add(lblNewLabel);
    
    JLabel lblHeight = new JLabel("Height(cm)");
    lblHeight.setBounds(25, 57, 87, 15);
    frame.getContentPane().add(lblHeight);
    
    tF1 = new JTextField();
    tF1.setBounds(113, 57, 87, 19);
    frame.getContentPane().add(tF1);
    tF1.setColumns(10);
    
    JLabel lblWeight = new JLabel("Weight(Kg)");
    lblWeight.setBounds(25, 96, 87, 15);
    frame.getContentPane().add(lblWeight);
    
    tF2 = new JTextField();
    tF2.setColumns(10);
    tF2.setBounds(113, 94, 87, 19);
    frame.getContentPane().add(tF2);
    
    JLabel lblGender = new JLabel("Gender");
    lblGender.setBounds(25, 123, 70, 15);
    frame.getContentPane().add(lblGender);
    
    JRadioButton rdbtnMale = new JRadioButton("MALE");
    rdbtnMale.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        gen="MALE";
      }
    });
    rdbtnMale.setBounds(25, 139, 70, 23);
    frame.getContentPane().add(rdbtnMale);
    
    JRadioButton rdbtnFemale = new JRadioButton("FEMALE");
    rdbtnFemale.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        gen="FEMALE";
      }
    });
    rdbtnFemale.setBounds(99, 139, 87, 23);
    frame.getContentPane().add(rdbtnFemale);
    
    JRadioButton rdbtnOther = new JRadioButton("Other");
    rdbtnOther.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        gen="OTHER";
      }
    });
    rdbtnOther.setBounds(183, 139, 81, 23);
    frame.getContentPane().add(rdbtnOther);
    genGP = new ButtonGroup();
    genGP.add(rdbtnMale);
    genGP.add(rdbtnFemale);
    genGP.add(rdbtnOther);
    JLabel lblAge = new JLabel("DOB");
    lblAge.setBounds(25, 174, 70, 15);
    frame.getContentPane().add(lblAge);
    
    JButton btnSubmit = new JButton("Submit");
    btnSubmit.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent arg0) {
        calculate_bmi();
      }
    });
    btnSubmit.setBounds(20, 215, 92, 25);
    frame.getContentPane().add(btnSubmit);
    
    JButton btnReset = new JButton("Reset");
    btnReset.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        he="";
        we="";
        res="";
        day="";
        month="";
        year="";
        gen="";
        tF1.setText("");
        tF2.setText("");
        cB1.setSelectedIndex(0);
        cB2.setSelectedIndex(0);
        cB3.setSelectedIndex(0);
        rdbtnMale.setSelected(true);
      }
    });
    btnReset.setBounds(172, 215, 92, 25);
    frame.getContentPane().add(btnReset);
    cB1 = new JComboBox(dates);
    cB1.setBounds(99, 169, 42, 24);
    frame.getContentPane().add(cB1);
    cB2 = new JComboBox(months);
    cB2.setBounds(139, 169, 47, 24);
    frame.getContentPane().add(cB2);
    cB3 = new JComboBox(years);
    cB3.setBounds(183, 169, 61, 24);
    frame.getContentPane().add(cB3);
  }
  public void calculate_bmi() {
    if(tF1.getText().isEmpty() || tF2.getText().isEmpty() || gen.isEmpty())
      {erro();
      return;
      }
    double h,w,r;
    he = tF1.getText();
    we = tF2.getText();
    day    = dates[cB1.getSelectedIndex()];
    month    = months[cB2.getSelectedIndex()];
    year    = years[cB3.getSelectedIndex()];
    h=Double.parseDouble(he);
    w=Double.parseDouble(we);
    r=w/Math.pow((h/100), 2);
    DecimalFormat df = new DecimalFormat("###.##");
    res="";
    res+=String.valueOf(df.format(r));
    if (r >= 25)
     res+="\t Overweight \n You have a higher than normal body weight. \nTry to exercise more.";
    else if (r > 18.5)
     res+="\t Normal \n You have normal body weight.\n Good Job!.";
    else
      res+="\t Underweight \n You have a lower than normal body weight.\n You can eat a it more.";
    JFrame f =new JFrame();  
      JOptionPane.showMessageDialog(f,res);      
  }
  public void erro() {
    JFrame f =new JFrame();  
      JOptionPane.showMessageDialog(f,"Fill all the details","Alert",JOptionPane.WARNING_MESSAGE);  
  }
}