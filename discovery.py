import os
import shutil
import sys

def detect_platform():
    """Detects the current agentic environment."""
    if os.getenv("ANTIGRAVITY_VERSION") or shutil.which("ag"):
        return "antigravity"
    if shutil.which("claude"):
        return "claude_code"
    if os.getenv("CODEX_HOME"):
        return "codex"
    return "generic"

def get_available_models():
    """Scans for available models based on environment variables or defaults."""
    platform = detect_platform()
    
    # Antigravity Profile
    if platform == "antigravity":
        return {
            "chairman": "gemini-3.1-pro-high",
            "members": ["gemini-3.1-pro-low", "gemini-3-flash", "claude-sonnet-4.6"]
        }
    
    # Claude Code Profile
    if platform == "claude_code":
        return {
            "chairman": "claude-3-5-sonnet",
            "members": ["claude-3-haiku", "claude-3-opus"]
        }
    
    # Generic / OpenRouter Fallback
    if os.getenv("OPENROUTER_API_KEY"):
        return {
            "chairman": "anthropic/claude-3-5-sonnet",
            "members": ["google/gemini-flash-1.5", "openai/gpt-4o-mini"]
        }
    
    # Absolute Fallback (Standard OpenAI/Anthropic env vars)
    if os.getenv("ANTHROPIC_API_KEY"):
        return {
            "chairman": "claude-3-5-sonnet",
            "members": ["claude-3-haiku"]
        }
    
    return {
        "chairman": "gpt-4o-mini", # Generic default
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
