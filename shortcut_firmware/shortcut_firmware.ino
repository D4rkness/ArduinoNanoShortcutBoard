#include <LedInterface.h>

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

// Enum for the keystates pressed, released or none
enum KeyState {PRESSED, RELEASED, NONE};

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

// Enables the mode to change the color
bool colorChangeMode = false;

// Interface to the Leds
LedInterface ledInterface;

// Init Setupmethod
void setup()
{
  ledInterface = LedInterface();
  ledInterface.init(13);
  ledInterface.toggleOnState();
  for (int i = 0; i < numPins; i++)
  {
    pinMode(allSwitchIds[i], INPUT);
  }


  Serial.begin(115200);
}

void loop()
{
  keyInputProcessing();
  ledInterface.ledMainLoop();
}

// The main logic of the board inputs and the state changes into the colormode and the firing of the commands to the pc
void keyInputProcessing(){
 for(int i = 0; i < numPins; i++){
    KeyState btnState = btnUnbouncedPressed(i);
    if( btnState == PRESSED  && !colorChangeMode){
      if(switchStates == 65){ // 65 is the Equivalent bitmask for f1 and f7 pressed (0000000010000001)
        colorChangeMode = true;
        Serial.println("[DBG]Colormode Enabled");
      }
    } else if (btnState == PRESSED && colorChangeMode){
      changColorMode(i);
    } else if(btnState == RELEASED && !colorChangeMode){
      Serial.println(btnCmdPrefix + (String)i);
    } else if(btnState == RELEASED && colorChangeMode){
      if(getSetBits() < 1){
        colorChangeMode = false;
        Serial.println("[DBG]Colormode Disabled");
      }
    }
  }
}


// Unbouncing the button pressed by comparing the timestamp and if the waitTime is big enough and the button is still pressed
// then button gets triggered and the command gets send
KeyState btnUnbouncedPressed(int btnId){

  unsigned long currentMillis = millis();
  uint16_t mask = 1UL << btnId;
  if(digitalRead(allSwitchIds[btnId]) && (currentMillis - unbouncingButtonTime[btnId] >= waitTime ) && !(switchStates & mask)){

      switchStates |= 1UL << btnId;
      unbouncingButtonTime[btnId] = currentMillis;
    return PRESSED;
  } else if(!digitalRead(allSwitchIds[btnId]) && (switchStates & mask)) {

    unbouncingButtonTime[btnId]= currentMillis;
    switchStates &= ~(1UL << btnId);
    return RELEASED;
  }
  return NONE;
}

// Returns the number of set bits in the switchState mask
uint8_t getSetBits(){
  uint8_t bitCounter = 0;
  uint16_t bufferStates = switchStates;
  while(bufferStates){
      bitCounter += bufferStates & 1; 
      bufferStates >>= 1; 
  }
  return bitCounter;
}

// When button f1 and f7 are pressed at the same time then color mode can be changed with the remaining buttons
// f1 + f7  (Buttoncombination) + 
// The following modes are mapped with the keyposition in the array (Number in the braces)
// f2(1) (Mode 1)  -> toggle on and off
// f3(2) (Mode 2) -> fix
// f4(3) (Mode 3) -> rainbow
// f5(4) (Mode 4) -> fade
// f6(5) (Mode 5) -> running
// f8(7) (Mode 6) -> ?
// f9(8) (Mode 7) -> ?
// f10(9) (Mode 8) -> ?
// f11(10) (Mode 9) -> ?
// f12(11) (Mode 10) -> ?

void changColorMode(int mode){
  switch(mode){
    case 1:
      ledInterface.toggleOnState();
      break;
    case 2:
      ledInterface.setColorMode(LedInterface::LedModes::FIX_COLOR);
      break;
    case 3:
      ledInterface.setColorMode(LedInterface::LedModes::RAINBOW);
      break;
    case 4:
      ledInterface.setColorMode(LedInterface::LedModes::LIGHTNING);
      break;
    case 5:
      ledInterface.setColorMode(LedInterface::LedModes::RUNNING);
      break;
    case 7:
      ledInterface.setColorMode(LedInterface::LedModes::FILLED_RUNNING);
      break;
    case 8:
      ledInterface.setColorMode(LedInterface::LedModes::SIDE_CENTER_RUNNING);
      break;
    case 9:

      break;
    case 10:

      break;
    case 11:
      ledInterface.setColorMode(LedInterface::LedModes::STROBE);
      break;
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
