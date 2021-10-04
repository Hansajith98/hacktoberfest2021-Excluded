#include <ESP8266WiFi.h>

const char* ssid     = "";
const char* password = "";

WiFiServer server(80);

String header;

String LED1_State = "off";


const int LED_1 = LED_BUILTIN;

// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0; 
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;

void setup() {
  Serial.begin(115200);
  
  pinMode(LED_1, OUTPUT);
 
  digitalWrite(LED_1, HIGH);

  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.print("IP address : ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop(){
  WiFiClient client = server.available();   // Listen for incoming clients

  if (client) {                             // If a new client connects,
    Serial.println("New Client");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    currentTime = millis();
    previousTime = currentTime;
    while (client.connected() && currentTime - previousTime <= timeoutTime) { // loop while the client's connected
      currentTime = millis();         
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        header += c;
        if (c == '\n') {                    // if the byte is a newline character
          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            
            // turns the LEDs on and off
            if (header.indexOf("GET /1/on") >= 0) {
              Serial.println("LED 1 on");
              LED1_State = "on";
              digitalWrite(LED_1, LOW);
            } else if (header.indexOf("GET /1/off") >= 0) {
              Serial.println("LED 1 off");
              LED1_State = "off";
              digitalWrite(LED_1, HIGH);
            }
            
            // Display the HTML web page
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}");
            client.println(".head { position: fixed; left: 0; top: 0; width: 100%; background-color: #34495e; font-size:35px; font-weight: bold; color: white; text-align: center; }");
            client.println(".footer { position: fixed; left: 0; bottom: 0; background-color: #34495e; width: 100%; color: white; text-align: center;}");
            client.println(".button { background-color: #c0392b; border: none; color: white; padding: 16px 40px; width: 150px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
            client.println(".button2 {background-color: #77878A; width: 150px;}</style></head>");
            
            // Web Page Heading
            client.println("<div class=\"head\"> <p>Hansajith's Home</p> </div></br></br></br></br></br></br></br>");
          
            client.println("<h3>LED 1</h3>");
            // If the LED1_State is off, it displays the ON button       
            if (LED1_State=="off") {
              client.println("<p><a href=\"/1/on\"><button class=\"button button2\">OFF</button></a></p>");
            } else {
              client.println("<p><a href=\"/1/off\"><button class=\"button\">ON </button></a></p>");
            } 

            client.println("</body></html>");
            client.println();
            break;
          } else { 
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    // Clear the header variable
    header = "";
    // Close the connection
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }
}
