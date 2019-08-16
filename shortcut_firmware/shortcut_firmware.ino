// Input of the Keys with their connected pin
#define F1_INPUT 2
#define F2_INPUT 3
#define F3_INPUT 4
#define F4_INPUT 5
#define F5_INPUT 6
#define F6_INPUT 7
#define F7_INPUT 8
#define F8_INPUT 9
#define F9_INPUT 10
#define F10_INPUT 11
#define F11_INPUT 12
#define F12_INPUT 15 // A0

// Total amount of Keys
#define numPins 12

// Pin of the WS2812b Leds
#define LED_PIN 13

// All switch ids inside of an array for easier acces
uint8_t allSwitchIds[] = {F1_INPUT,
                          F2_INPUT,
                          F3_INPUT,
                          F4_INPUT,
                          F5_INPUT,
                          F6_INPUT,
                          F7_INPUT,
                          F8_INPUT,
                          F9_INPUT,
                          F10_INPUT,
                          F11_INPUT,
                          F12_INPUT};

// Prefix for button command
String btnCmdPrefix = "[CMD][PRS]";

// Here a 16 bit integer, but only the first 12 bits are used
uint16_t switchStates = 0;

// Saved times for unbouncing the buttons
long unbouncingButtonTime [numPins];

// Waittime for btnUnbouncing
long waitTime = 80;

// Init Setupmethod
void setup()
{
  //FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  for (int i = 0; i < numPins; i++)
  {
    pinMode(allSwitchIds[i], INPUT);
  }
  Serial.begin(9600);
}

void loop()
{
  for(int i = 0; i < numPins; i++){
    btnUnbouncedPressed(i);
  }
  
}

// Unbouncing the button pressed by comparing the timestamp and if the waitTime is big enough and the button is still pressed
// then button gets triggered and the command gets send
void btnUnbouncedPressed(int btnId){

  unsigned long currentMillis = millis();
  uint16_t mask = 1<<btnId;
  if(digitalRead(allSwitchIds[btnId]) && (currentMillis - unbouncingButtonTime[btnId] >= waitTime ) && !(switchStates & mask)){

      Serial.println(btnCmdPrefix + (String)btnId);
      switchStates |= 1UL << btnId;
      unbouncingButtonTime[btnId] = currentMillis;

  } else if(!digitalRead(allSwitchIds[btnId]) && (switchStates & mask)) {

    unbouncingButtonTime[btnId]= currentMillis;
    switchStates &= ~(1UL << btnId);

  }
}

    // For Debuggign printing bitarray
 void printBitArrayDebug(unsigned n)
{
  int k;
  Serial.print("[DBG]");
  for (int c = 16; c >= 0; c--){

    k = n >> c;

    if (k & 1)
      Serial.print("1");
    else
      Serial.print("0");
  }

  Serial.print("\n");
}
