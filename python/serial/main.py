import serial
import time

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")

serial_port = serial.Serial(
    port=
)

time.sleep(1)

try:
    serial_port.write("UART Demonstration Program\r\n".encode())
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.read()
            print(data)
            serial_port.write(data)
            if data == "\r".encode():
                serial_port.write("\n".encode())

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass