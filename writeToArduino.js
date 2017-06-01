var SerialPort = require('serialport')

var port = new SerialPort('/dev/cu.usbmodem1411', { baudRate: 9600 })

port.on('open', function() {
  port.write('9')
})
