import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="server.crt",
                           cert_reqs=ssl.CERT_REQUIRED,
                           ciphers = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES128-SHA256:HIGH:")

ssl_sock.connect(('localhost', 10035))

while  True:
    mensaje = raw_input("Mensaje  a enviar: ")

#invoco  el metodo send pasando como parametro el string ingresado por el  usuario
    ssl_sock.write(mensaje)
    ssl_sock.close()
