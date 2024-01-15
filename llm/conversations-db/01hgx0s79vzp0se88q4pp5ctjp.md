**Prompt:**
March 2023 - Making Firefox on Linux work with pi-hole

**Response:**
To make Firefox on Linux work with Pi-hole, ensure that Firefox is configured to use the DNS settings provided by the operating system, where Pi-hole is set as the DNS server. Here's a step-by-step guide:

1. **Set Pi-hole as DNS server**: Configure your network settings on Linux to use Pi-hole as the DNS server. This is typically done by setting the Pi-hole's IP address as the DNS server in your network configuration or router settings.

2. **Disable Firefox's DNS-over-HTTPS (DoH)**: By default, Firefox may use DoH, which bypasses the system's DNS settings. Disable this feature to ensure Firefox uses the Pi-hole DNS.
   - Type `about:config` in the Firefox address bar and press Enter.
   - Search for `network.trr.mode` and set its value to `5`. This disables DoH.

3. **Verify DNS configuration**:
   - Restart Firefox and visit a website.
   - Check the Pi-hole dashboard to see if the DNS requests are being logged.

4. **Troubleshoot**: If Firefox is not using Pi-hole after these steps, check for any other DNS settings within Firefox that might be overriding the system DNS settings, and ensure that there are no proxy settings enabled that could bypass the DNS settings.

5. **Test**: To test if Pi-hole is working with Firefox, try accessing a known ad-serving domain and see if it gets blocked by Pi-hole.

If you encounter issues, ensure that there are no other network configurations on your Linux system that might be overriding the DNS settings to something other than Pi-hole.

<details><summary>Metadata</summary>

- Duration: 21518 ms
- Datetime: 2023-12-05T12:55:32.908502
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

