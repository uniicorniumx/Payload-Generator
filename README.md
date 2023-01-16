# Payload-Generator

This script defines three lists of payloads, one for each vulnerability type: XSS, RCE, and SQL injection, and store them in a dictionary. The get_payloads function takes a single argument, the type of vulnerability, and returns a list of payloads from the corresponding key in the dictionary. If the passed argument is not a valid key in the dictionary, it will return a string indicating the available types.
