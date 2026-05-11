import os
import shutil
import sys
from pathlib import Path

def detect_platform():
    """Detects the current agentic environment with fallback for Windows folders."""
    # 1. Check for commands in PATH
    if shutil.which("ag"):
        return "antigravity"
    
    # 2. Robust check for Antigravity data folder (Windows)
    antigravity_path = Path.home() / ".gemini/antigravity"
    if antigravity_path.exists():
        return "antigravity"
        
    if shutil.which("claude"):
        return "claude_code"
    if os.getenv("CODEX_HOME"):
        return "codex"
    return "generic"

def get_available_models():
    """Scans for available models based on environment variables or defaults."""
    platform = detect_platform()
    
    # Antigravity Profile (Full 5 Members + Chairman)
    if platform == "antigravity":
        return {
            "chairman": "gemini-3.1-pro-high",
            "members": [
                "gemini-3.1-pro-low", 
                "gemini-3-flash", 
                "claude-sonnet-4.6", 
                "claude-opus-4.6", 
                "gpt-oss-120b-medium"
            ]
        }
    
    # Claude Code Profile
    if platform == "claude_code":
        return {
            "chairman": "claude-3-5-sonnet",
            "members": ["claude-3-haiku", "claude-3-opus"]
        }
    
    # Fallback Profile
    return {
        "chairman": "gpt-4o-mini",
        "members": ["gpt-4o-mini"]
    }

def auto_configure_council():
    """Returns the final configuration for the council orchestration."""
    models = get_available_models()
    return {
        "platform": detect_platform(),
        "chairman": models["chairman"],
        "council_members": models["members"]
    }
