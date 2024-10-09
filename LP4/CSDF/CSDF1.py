import email
import re

# Sample email header (as a string)
email_header = """
Received: from mail.example.com (mail.example.com [198.51.100.2]) by smtp.mailserver.com with ESMTP id ABCD1234 for <victim@example.com>; Thu, 05 Oct 2024 10:14:58 -0400 (EDT)
From: attacker@example.com
To: victim@example.com
Subject: Suspicious Activity Alert
Date: Thu, 05 Oct 2024 10:14:58 -0400
Message-ID: <1234567890@example.com>
"""

# Function to extract the relevant information from email header
def analyze_email_header(header):
    analysis_result = {}

    # Extract the "From" field
    from_match = re.search(r'From:\s*(.*)', header)
    if from_match:
        analysis_result['From'] = from_match.group(1)

    # Extract the "To" field
    to_match = re.search(r'To:\s*(.*)', header)
    if to_match:
        analysis_result['To'] = to_match.group(1)

    # Extract the "Subject" field
    subject_match = re.search(r'Subject:\s*(.*)', header)
    if subject_match:
        analysis_result['Subject'] = subject_match.group(1)

    # Extract the "Date" field
    date_match = re.search(r'Date:\s*(.*)', header)
    if date_match:
        analysis_result['Date'] = date_match.group(1)

    # Extract the "Message-ID" field
    message_id_match = re.search(r'Message-ID:\s*(.*)', header)
    if message_id_match:
        analysis_result['Message-ID'] = message_id_match.group(1)

    # Extract the IP address from "Received" field (shows the sender's mail server and intermediate hops)
    received_ips = re.findall(r'\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]', header)
    if received_ips:
        analysis_result['Received IPs'] = received_ips

    return analysis_result

# Analyze the provided email header
email_analysis = analyze_email_header(email_header)

# Print the analysis result
for key, value in email_analysis.items():
    print(f"{key}: {value}")
