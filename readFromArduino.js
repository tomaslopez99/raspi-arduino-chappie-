var SerialPort = require('serialport')
var shell = require('shell')

var port = new SerialPort('/dev/cu.usbmodem1411', { baudRate: 9600 })

port.on('data', function(info) {
  if(info == 4) {
    shell.run('4.py')
  }

  if(info == 6) {
    shell.run('6.py')
  }
})
