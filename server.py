import sys
import subprocess
import os

# 1. Self-Installation / Dependency Check
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(">>> Dependency 'mcp' not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mcp"])
    from mcp.server.fastmcp import FastMCP

from discovery import auto_configure_council, detect_platform
from installer import check_and_install
from logic import run_deliberation_logic

# 2. Silent Auto-Registration
check_and_install()

# 3. Initialize Smart Server
platform = detect_platform()
council_config = auto_configure_council()

mcp = FastMCP(f"LLM Council ({platform.upper()})")

@mcp.tool()
async def deliberate(query: str) -> str:
    """
    Triggers a 3-stage LLM deliberation council.
    Automatically uses the best agents detected in your environment.
    """
    result = await run_deliberation_logic(query, council_config)
    
    return f"""
# RESULTADO DEL CONSEJO ({platform.upper()})

## Resumen Ejecutivo
{result['summary']}

---

## Razonamiento por Etapas
{result['detailed_reasoning']}

---
*Configuracion: Chairman={council_config['chairman']}, Miembros={len(council_config['council_members'])}*
"""

if __name__ == "__main__":
    # Removed emojis to prevent UnicodeEncodeError on Windows
    print(f"\n[SERVER] Servidor MCP '{mcp.name}' iniciado correctamente.")
    print(f"[*] Entorno detectado: {platform.upper()}")
    print(f"[*] Chairman asignado: {council_config['chairman']}")
    print(f"[*] Miembros activos: {len(council_config['council_members'])}")
    print("\n[INFO] El servidor esta bloqueado escuchando peticiones JSON-RPC (stdin).")
    print("[INFO] Si ya ves el mensaje de registro arriba, puedes cerrar esta terminal.")
    print("Para forzar salida: Ctrl+C\n")
    mcp.run()
