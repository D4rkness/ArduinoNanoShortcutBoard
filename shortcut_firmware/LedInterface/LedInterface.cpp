#include "LedInterface.h"


void LedInterface::init(uint8_t dataPin){
    FastLED.addLeds<WS2812B, 13, GRB>(leds, NUM_LEDS); // Todo: Change the 13 here to the datapin 
}

void LedInterface::ledMainLoop(){
    if(isLightOff){
        switch(currMode){
            case FIX_COLOR:
                fill_solid(this->leds, NUM_LEDS, CRGB(this->red,this->green,this->blue));
                FastLED.show();
            break;
    }
        
    } else {
        fill_solid(this->leds, NUM_LEDS, CRGB::Black);
        FastLED.show();
    }

    
    
}


////////////////////////////////////////
// Methods to Change the internal States 
void LedInterface::toggleOnState(){
    isLightOff = !isLightOff;
}

void LedInterface::setColorMode(LedModes ledMode){
    this->currMode = ledMode;
}

