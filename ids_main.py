from scapy.all import sniff
import time
from logging_setup import setup_logger  
from ids_analysis import detect_anomalies


logger = setup_logger()
logger.info("IDS started.")


monitored_ports = [80, 443, 53, 25, 110, 143, 21, 22, 3389]
monitored_ports_activity = {port: False for port in monitored_ports}


captured_packets = []


def packet_callback(packet):
    if packet.haslayer('TCP') or packet.haslayer('UDP'):
        src_port = getattr(packet, 'sport', 'N/A')
        dst_port = getattr(packet, 'dport', 'N/A')

        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
        else:
            src_ip = "unknown"
            dst_ip = "unknown"

        proto = "TCP" if packet.haslayer('TCP') else "UDP"
        packet_summary = f"{proto} {src_ip}:{src_port} > {dst_ip}:{dst_port}"

        logger.info(f"Packet captured: {packet_summary}")

        
        if src_port in monitored_ports:
            monitored_ports_activity[src_port] = True
        if dst_port in monitored_ports:
            monitored_ports_activity[dst_port] = True

        
        captured_packets.append({
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Source Port": src_port,
            "Destination Port": dst_port,
            "Protocol": proto,
            "Packet Summary": packet_summary
        })


ports = "tcp or udp"


total_packets = 50
packets_per_interval = 5
interval = 2

for _ in range(total_packets // packets_per_interval):
    sniff(filter=ports, prn=packet_callback, count=packets_per_interval, timeout=interval)
    time.sleep(interval)


for port, activity in monitored_ports_activity.items():
    if not activity:
        logger.info(f"No packet flow on port {port}")

# Anormallik analizi yap
logger.info("Starting packet analysis.")
detect_anomalies(captured_packets)
logger.info("Packet analysis completed.")
