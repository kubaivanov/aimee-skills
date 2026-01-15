import json
import requests
import sys
import os
from pathlib import Path
from urllib.parse import urljoin

def deploy(json_path, sse_url=None):
    if not sse_url:
        # Try to get from environment or use the known working one
        sse_url = os.getenv("FRAMER_MCP_URL", "https://mcp.unframer.co/sse?id=9b3f53d2ebdb0edfc9c452a48a08e46cd6c90ffbe2d45617a3fe648e05e5e8b9&secret=imc5NhmsnBljdnTCB3iweC7ZCD1EBo97")

    print(f"Connecting to Framer MCP via: {sse_url}")
    
    try:
        # 1. Establish SSE connection to get message endpoint
        response = requests.get(sse_url, stream=True, timeout=10)
        endpoint_url = None
        
        for line in response.iter_lines():
            if not line:
                continue
            line_text = line.decode('utf-8')
            if line_text.startswith("data: "):
                endpoint_url = line_text[6:]
                if not endpoint_url.startswith("http"):
                    endpoint_url = urljoin("https://mcp.unframer.co", endpoint_url)
                break
                
        if not endpoint_url:
            print("Error: Could not retrieve endpoint URL from SSE.")
            return False

        # 2. Load article data
        with open(json_path, 'r', encoding='utf-8') as f:
            article_data = json.load(f)

        # 3. Prepare JSON-RPC request
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "upsertCMSItem",
                "arguments": {
                    "collectionId": article_data.get("collectionId", "A7DWNZVX_"),
                    "slug": article_data.get("slug"),
                    "draft": article_data.get("draft", True),
                    "fieldData": article_data["fieldData"]
                }
            }
        }

        # 4. Send request
        print(f"Upserting article '{article_data.get('slug')}' to Framer...")
        res = requests.post(endpoint_url, json=payload, timeout=30)
        
        if res.status_code in [200, 202]:
            result = res.json() if res.status_code == 200 else {"status": "accepted"}
            if "error" in result:
                print(f"MCP Error: {json.dumps(result['error'], indent=2, ensure_ascii=False)}")
                return False
            else:
                print("✓ Article successfully queued/uploaded to Framer.")
                return True
        else:
            print(f"HTTP Error: {res.status_code}")
            print(res.text)
            return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 framer_upsert.py <path_to_article.json> [sse_url]")
        sys.exit(1)
    
    success = deploy(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    sys.exit(0 if success else 1)
