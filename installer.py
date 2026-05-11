import json
import os
import sys
from pathlib import Path

def check_and_install():
    """
    Quietly registers the MCP server in the local configuration if not present.
    Supports VSCode/Cursor (Claude Dev / Roo Code) standard paths.
    """
    if os.name == "nt": # Windows
        config_dir = Path(os.getenv("APPDATA")) / "Code/User/globalStorage/saoudrizwan.claude-dev/settings"
    else: # macOS/Linux
        config_dir = Path.home() / "Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings"
    
    config_path = config_dir / "mcp_config.json"
    
    if not config_path.exists():
        # Try alternate path for Roo Code
        config_path = config_path.parent.parent.parent / "roovet.roo-ignore/settings/mcp_config.json"
        if not config_path.exists():
            return

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        
        server_name = "llm-council-smart"
        server_path = str(Path(__file__).parent / "server.py")
        
        # Check if already registered
        servers = config.get("mcpServers", {})
        if server_name not in servers:
            config.setdefault("mcpServers", {})[server_name] = {
                "command": sys.executable,
                "args": [server_path],
                "env": {"SMART_MCP_AUTO": "true"},
                "disabled": False
            }
            
            with open(config_path, "w") as f:
                json.dump(config, f, indent=2)
            print(f">>> [MCP] Council registered automatically in {config_path.name}")
    except Exception as e:
        # Silent fail to not disrupt the main process
        pass

if __name__ == "__main__":
    check_and_install()
