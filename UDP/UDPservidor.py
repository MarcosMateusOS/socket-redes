import socket


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

bytesToSend         = str.encode(msgFromServer)

# Cria socket datagram (UDP)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind entre endereco e IP
UDPServerSocket.bind((localIP, localPort))
 
print("Servidor UDP up e escutando...")


def calculate(values):
    value1 = int(values[0])
    value2 = int(values[1])
    operator = str(values[2])

    match operator:
        case '+':
            return value1 + value2
        
        case '-':
            return value1 - value2

        case '*':
            return value1 * value2

        case '/':
            return value1 / value2




# Escutando datagramas que chegam
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    strMessage = message.decode("UTF-8")
    splitedMessage = strMessage.split(", ")
    result = calculate(splitedMessage)
    clientMsg = "Mensagem do Cliente:{}".format(result)
    clientIP  = "Endereco IP do Cliente:{}".format(address)
    
    print(result)
    print(clientIP)

    # Enviando msg de reply ao client
    UDPServerSocket.sendto(str.encode(str(result)), address)