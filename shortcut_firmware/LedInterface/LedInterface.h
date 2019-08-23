#ifndef _LEDINTERFACE_H_
#define _LEDINTERFACE_H_

#include <FastLED.h>
#include <Arduino.h>
#define NUM_LEDS 14

class LedInterface{

    public:
        enum LedModes {FIX_COLOR, RAINBOW, FADE, RUNNING, FILLED_RUNNING, SIDE_CENTER_RUNNING, LIGHTNING, STROBE};
        static LedModes modes;
        
    public:
        void init(uint8_t dataPin);
        
        // Mainloop for the handling of the led scene display
        void ledMainLoop();

        // Commands from the keyboard for the colormodechange
        void toggleOnState();
        void setColorMode(LedModes ledMode);

        // Commands from the pc app to change the colorconfig
        void setColor(String colorHexString);

    private:
        int red = 255;
        int blue = 255;
        int green = 255;

        bool isInitialized = false;
        bool isLightOff = false;

        LedModes currMode = FIX_COLOR;
        
        CRGB leds[NUM_LEDS];

        
        // Representation of the Modes as Method, all relevant data is inside of them
        void fixColorMode();
        void rainbowMode();
        void fadeMode();
        void runningMode();
        void filledRunningMode();
        void sideCenterRunningModes();
        void lightningMode();
        void strobeMode();
        void initAnimation();
        void clearAllLeds();

};

#endif