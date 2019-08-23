#include "LedInterface.h"


void LedInterface::init(uint8_t dataPin){
    FastLED.addLeds<WS2812B, 13, GRB>(leds, NUM_LEDS); // Todo: Change the 13 here to the datapin 
    initAnimation();
}

void LedInterface::ledMainLoop(){
    if(isLightOff){
        switch(currMode){
            case FIX_COLOR:
                fixColorMode();
            break;
            case RAINBOW:
                rainbowMode();
            break;
            case FADE:
                fadeMode();
            break;
            case RUNNING:
                runningMode();
            break;
            case FILLED_RUNNING:
                filledRunningMode();
            break;
            case SIDE_CENTER_RUNNING:
                sideCenterRunningModes();
            break;
            case LIGHTNING:
                lightningMode();
            break;    
            case STROBE:
                strobeMode();
            break;         
        }
        
    } else {
        fill_solid(this->leds, NUM_LEDS, CRGB::Black);
        FastLED.show();
    }

}

///////////////////
// fixColorMode paramter
int oldRed = 0;
int oldGreen = 0;
int oldBlue = 0;

void LedInterface::fixColorMode(){
    //if(this->red != oldRed && this->green != oldGreen && this->blue != oldBlue){
        fill_solid(this->leds, NUM_LEDS, CRGB(this->red,this->green,this->blue));
        oldRed = this->red;
        oldGreen = this->green;
        oldBlue = this-> blue;
        FastLED.show();
    //}
}

///////////////////
// rainbowMode paramter
uint8_t rainbowHue = 0;
void LedInterface::rainbowMode(){
    fill_rainbow( leds, NUM_LEDS, rainbowHue, 7);
    EVERY_N_MILLISECONDS( 20 ) { rainbowHue++; }
    FastLED.show();
}

///////////////////
// fadeMode paramter

void LedInterface::fadeMode(){

}

///////////////////
// runningMode paramter
int runningDelay = 100;
int runningSingleCounter = 6;
void LedInterface::runningMode(){
    EVERY_N_MILLISECONDS( runningDelay ) {
            if(runningSingleCounter < 0){
                runningSingleCounter = NUM_LEDS - 1;
            }
            clearAllLeds();
            leds[runningSingleCounter--] = CRGB(this->red,this->green,this->blue);
            FastLED.show();

    }
}

///////////////////
// filledRunningMode paramter
int runningFullDelay = 100;
int runningFullCoutner = 0;
bool isFullFinished = false;

void LedInterface::filledRunningMode(){
    EVERY_N_MILLISECONDS( runningFullDelay ) {
            if(runningFullCoutner >= NUM_LEDS){
                runningFullCoutner = 0;
                isFullFinished = !isFullFinished;
            }
            if(isFullFinished){
                leds[runningFullCoutner++] = CRGB::Black;
            } else {
                leds[runningFullCoutner++] = CRGB(this->red,this->green,this->blue);
            }
            
            FastLED.show();

    }
}

///////////////////
// sideCenterRunningModes paramter
bool isColorCenterRunningFinished = false;
int sideCenterRunningDelay = 100;
int sideCenterCounter = 0;
int oneRowLeds = NUM_LEDS / 2;
int oneEavenLedNumExtra = oneRowLeds % 2;
CRGB centerRunningColor = CRGB::Black;

void LedInterface::sideCenterRunningModes(){
    EVERY_N_MILLISECONDS(sideCenterRunningDelay) {
        if(!isColorCenterRunningFinished){
            centerRunningColor = CRGB(this->red,this->green,this->blue);
        } else {
            centerRunningColor = CRGB::Black;
        }

        if(sideCenterCounter < oneRowLeds /2){

            leds[sideCenterCounter] = centerRunningColor;
            leds[sideCenterCounter + oneRowLeds] = centerRunningColor;
            leds[oneRowLeds - 1 - sideCenterCounter] = centerRunningColor;
            leds[NUM_LEDS - sideCenterCounter - 1] = centerRunningColor;
            sideCenterCounter++;
        } else if(sideCenterCounter < oneRowLeds /2 + 1 && oneEavenLedNumExtra != 0){-
            leds[oneRowLeds/2] = centerRunningColor;
            leds[oneRowLeds/2 + oneRowLeds] = centerRunningColor;
            sideCenterCounter++;
        } else {
            isColorCenterRunningFinished = !isColorCenterRunningFinished;
            sideCenterCounter = 0;    
        }     
        FastLED.show();
    }
}

///////////////////
// Lightning paramter
uint8_t frequency = 50;     // controls the interval between strikes
uint8_t flashes = 8;        //the upper limit of flashes per strike
uint8_t ledstart;           // Starting location of a flash
uint8_t ledlen;             // Length of a flash
unsigned int dimmer = 1;
int flashCounter = 0;

void LedInterface::lightningMode(){
    ledstart = random8(NUM_LEDS);
    ledlen = random8(NUM_LEDS-ledstart);
  EVERY_N_MILLISECONDS( random8(frequency)*100 ) {
      EVERY_N_MILLISECONDS( 50+random8(100) ) {
            if(flashCounter == 0){
                EVERY_N_MILLISECONDS( 50+random8(100) ) {
                     for (int flashCounter = 0; flashCounter < random8(3,flashes); flashCounter++) {
                        if(flashCounter == 0) dimmer = 5;
                        else dimmer = random8(1,3);                        
                        fill_solid(leds+ledstart,ledlen,CHSV(255, 0, 255/dimmer));
                        FastLED.show();
                        delay(random8(4,10));                                     // each flash only lasts 4-10 milliseconds
                        fill_solid(leds+ledstart,ledlen,CHSV(255,0,0));           // Clear the section of LED's
                        FastLED.show();
                }
            }      
        }
      
    }
  }

}

///////////////////
// Strobe Parameter
bool isStrobeOn = false;
int strobeDelay = 30;
void LedInterface::strobeMode(){
    EVERY_N_MILLISECONDS(strobeDelay) {
        if(isStrobeOn){
            fill_solid(this->leds, NUM_LEDS, CRGB(this->red,this->green,this->blue));
            FastLED.show();
        } else {
            clearAllLeds();
        }
        isStrobeOn = !isStrobeOn;
    }
}

///////////////////
// Clearing all leds for animations
void LedInterface::clearAllLeds(){
    fill_solid(this->leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
}

///////////////////
// Animation for the boot up
void LedInterface::initAnimation(){
    for(int i = 0; i < NUM_LEDS; i++){
        leds[i] = CRGB(CRGB::Red);
        FastLED.show();
        delay(50);
    }
}


////////////////////////////////////////
// Methods to Change the internal States 
void LedInterface::toggleOnState(){
    isLightOff = !isLightOff;
}

void LedInterface::setColorMode(LedModes ledMode){
    this->currMode = ledMode;
    clearAllLeds();
}

