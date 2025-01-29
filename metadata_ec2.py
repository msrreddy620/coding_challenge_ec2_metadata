import requests
import json

AWS_METADATA_URL = "http://169.254.169.254/latest/meta-data/"
TOKEN_URL = "http://169.254.169.254/latest/api/token"

def get_metadata(key=None):
    """Fetch AWS instance metadata using IMDSv2 authentication."""
    try:
        # Step 1: Get the token 
        token_response = requests.put(TOKEN_URL, headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}, timeout=2)
        token_response.raise_for_status()
        token = token_response.text

        # Step 2: Fetch metadata using the token
        headers = {"X-aws-ec2-metadata-token": token}
        url = f"{AWS_METADATA_URL}{key}" if key else AWS_METADATA_URL
        
        response = requests.get(url, headers=headers, timeout=2)
        response.raise_for_status()

        # Format output
        if key:
            metadata = {key: response.text}
        else:
            metadata = {}
            for item in response.text.splitlines():
                sub_response = requests.get(f"{AWS_METADATA_URL}{item}", headers=headers, timeout=2)
                sub_response.raise_for_status()
                metadata[item] = sub_response.text

        return json.dumps(metadata, indent=4)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)}, indent=4)

if __name__ == "__main__":
    import sys
    key = sys.argv[1] if len(sys.argv) > 1 else None
    print(get_metadata(key))

