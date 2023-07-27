#include <iostream>
#include <random>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    // Set up the TCP connection
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in servaddr;
    std::memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(12345);  // change to desired port number
    inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr);  // change to Python program's IP address

    if (connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) != 0) {
        std::cerr << "Failed to connect to server\n";
        return 1;
    }
    
    // Generate random coordinates and send them to the Python program
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dist(0.0, 10.0);
    double coords[12];
    for (int i = 0; i < 6; i++) {
        coords[i*2] = dist(gen);
        coords[i*2+1] = dist(gen);
    }
    send(sockfd, (void*)coords, sizeof(coords), 0);
    
    // Close the TCP connection
    close(sockfd);
    return 0;
}
