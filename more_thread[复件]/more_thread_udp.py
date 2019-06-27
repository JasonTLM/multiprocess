# coding=utf-8
import socket
import threading


def send_msg(udp_socket, dest_ip, dest_port):
    # """获取键盘数据，并将其发送给对方"""
    # # 2. 输入对方的ip
    # dest_ip = input("\n请输入对方的IP地地址：")
    # # 3. 输入对方端口地址port
    # dest_port = input("\n请输入对方的端口port地址:")
    while True:
        # 1. 从键盘输入数据
        send_data = input('\n请输入要发送的数据：'+"\n")
        # 4. 发送数据
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))
        # udp_socket.sendto


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # print("\n")
        print(recv_data[0])


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7888))

    dest_ip = input("请输入对方IP地址：")
    dest_port = int(input("请输入对方的port："))

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()