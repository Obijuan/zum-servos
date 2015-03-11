/*
*   Client for the Zum Servo Server
*   
*   Control servos with Sliders
*   
*   (c) Juan Gonzalez Gomez (Obijuan). Feb-2015
*   GPL v2 license
*   
*/

//-- Setup the bluetooth connection
network.connectBluetoothSerialByUi(
function(m, data) {
      console.log(data);
});

//-- Create the servos
var a = new Servo('a');
var b = new Servo('b');
var c = new Servo('c');
var d = new Servo('d');

//------------------ Sliders for controlling the servos
var slider1 = ui.addSlider(20, 20, ui.sw - 20, -1, -90, 90,
function(progress){
    a.setpos(progress);
});

var slider2 = ui.addSlider(20, 150, ui.sw - 20, -1, -90, 90,
function(progress){
    b.setpos(progress);
});

var slider3 = ui.addSlider(20, 280, ui.sw - 20, -1, -90, 90,
function(progress){
    c.setpos(progress);
});

var slider3 = ui.addSlider(20, 410, ui.sw - 20, -1, -90, 90,
function(progress){
    d.setpos(progress);
});



//--------- Servo Class
function Servo(dir)
{
    this.dir = dir;    //-- Servo identificator
    this._pos = 0;     //-- Current servo pos
    
    //-- Set the servo position
    this.setpos = function(pos) {
        
        //-- Only integer positions
        pos = Math.round(pos);
        
        //-- Update the servo only if there is a change
        if (pos != this._pos) {
            network.sendBluetoothSerial(this.dir + pos + "\r");
            this._pos = pos;
            console.log(pos);
        }
    }
}



