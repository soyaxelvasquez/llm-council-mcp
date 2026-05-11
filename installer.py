import json
import os
import sys
from pathlib import Path

def check_and_install():
    """
    Registers the MCP server with detailed verbose output.
    Robust handling for empty/malformed config files.
    """
    print("\n--- [MCP SETUP] Iniciando Auto-Configuracion ---")
    
    paths = [
        Path.home() / ".gemini/antigravity/mcp_config.json",
        Path(os.getenv("APPDATA", "")) / "Code/User/globalStorage/saoudrizwan.claude-dev/settings/mcp_config.json",
        Path.home() / "Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/mcp_config.json"
    ]
    
    config_path = None
    print(f"[*] Buscando archivo de configuracion en {len(paths)} ubicaciones...")
    
    for p in paths:
        if p.exists():
            config_path = p
            print(f"[+] Encontrado: {p}")
            break
    
    if config_path is None:
        print("[!] ERROR: No se encontro ningun archivo mcp_config.json.")
        return

    try:
        content = ""
        with open(config_path, "r") as f:
            content = f.read().strip()
            
        if not content:
            print("[i] Archivo vacio. Inicializando...")
            config = {"mcpServers": {}}
        else:
            try:
                config = json.loads(content)
            except json.JSONDecodeError:
                print("[!] Error de formato JSON. Re-inicializando...")
                config = {"mcpServers": {}}
        
        server_name = "llm-council-smart"
        server_path = str(Path(__file__).parent.absolute() / "server.py")
        
        if "mcpServers" not in config:
            config["mcpServers"] = {}
            
        print(f"[*] Registrando servidor: '{server_name}'")
        config["mcpServers"][server_name] = {
            "command": sys.executable,
            "args": [server_path],
            "env": {"SMART_MCP_AUTO": "true"},
            "disabled": False
        }
        
        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)
        print(f"[SUCCESS] Registro completado en {config_path.name}")
            
    except Exception as e:
        print(f"[!] ERROR: {str(e)}")

    print("--- [MCP SETUP] Finalizado ---\n")

if __name__ == "__main__":
    check_and_install()
