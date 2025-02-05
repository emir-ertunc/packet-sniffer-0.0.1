from logging_setup import setup_logger
import pandas as pd


logger = setup_logger()


HIGH_TRAFFIC_THRESHOLD = 10

def detect_anomalies(packet_data):
    """
    Detects anomalies in the captured packets and logs them.
    """
    if not packet_data:
        logger.info("No packet data found for analysis.")
        return

   
    packet_df = pd.DataFrame(packet_data)

    monitored_ports = {80, 443, 53, 25, 110, 143, 21, 22, 3389}

    
    unknown_ports = packet_df[
        (~packet_df["Source Port"].isin(monitored_ports)) &
        (~packet_df["Destination Port"].isin(monitored_ports))
    ]
    if not unknown_ports.empty:
        logger.warning(f"{len(unknown_ports)} packets detected to/from unknown ports.")

    
    traffic_by_port = packet_df["Destination Port"].value_counts()
    high_traffic_ports = traffic_by_port[traffic_by_port > HIGH_TRAFFIC_THRESHOLD]
    if not high_traffic_ports.empty:
        logger.warning("High traffic detected:")
        for port, count in high_traffic_ports.items():
            logger.warning(f"Destination Port {port}: {count} packets")
            if count > HIGH_TRAFFIC_THRESHOLD * 5:
                logger.critical(f"Extremely high traffic on port {port} ({count} packets) - Possible DDoS attack.")

    
    unexpected_protocols = packet_df[
        ~packet_df["Packet Summary"].str.contains("TCP|UDP", na=False)
    ]
    if not unexpected_protocols.empty:
        logger.warning(f"{len(unexpected_protocols)} packets with unexpected protocols detected.")

    logger.info("Anomaly detection completed.")
