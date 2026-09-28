import json
import sys
from client import TruncatedSVD

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "truncated_svd",
                        "description": "Compute top k singular values and vectors for matrix",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "matrix": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}},
                                "k": {"type": "integer", "default": 2}
                            },
                            "required": ["matrix"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "truncated_svd":
            U, S, V = TruncatedSVD.power_svd(args["matrix"], k=args.get("k", 2))
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps({"singular_values": S, "U": U, "V": V})}]}
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
