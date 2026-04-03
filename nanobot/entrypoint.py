import json
import os

config_path = "/app/nanobot/config.json"
resolved_path = "/tmp/config.resolved.json"
workspace = "/app/nanobot/workspace"

with open(config_path) as f:
    config = json.load(f)

# LLM provider
config["agents"]["defaults"]["model"] = os.environ.get("LLM_API_MODEL", "coder-model")
config["providers"]["custom"] = {
    "apiKey": os.environ["LLM_API_KEY"],
    "apiBase": os.environ["LLM_API_BASE_URL"],
}
config["agents"]["defaults"]["provider"] = "custom"

# Gateway
config.setdefault("gateway", {})
config["gateway"]["host"] = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS", "0.0.0.0")
config["gateway"]["port"] = int(os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT", "18790"))

# LMS MCP server
config["tools"]["mcpServers"]["lms"]["env"] = {
    "NANOBOT_LMS_BACKEND_URL": os.environ["NANOBOT_LMS_BACKEND_URL"],
    "NANOBOT_LMS_API_KEY": os.environ["NANOBOT_LMS_API_KEY"],
}

# Observability MCP server
config["tools"]["mcpServers"]["obs"] = {
    "command": "python",
    "args": ["-m", "mcp_obs.server"],
    "env": {
        "NANOBOT_VICTORIALOGS_URL": os.environ.get("NANOBOT_VICTORIALOGS_URL", "http://victorialogs:9428"),
        "NANOBOT_VICTORIATRACES_URL": os.environ.get("NANOBOT_VICTORIATRACES_URL", "http://victoriatraces:10428"),
    }
}

# Webchat MCP server
webchat_port = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT", "8765")
access_key = os.environ.get("NANOBOT_ACCESS_KEY", "")
config["tools"]["mcpServers"]["webchat"] = {
    "command": "python",
    "args": ["-m", "mcp_webchat"],
    "env": {
        "MCP_WEBCHAT_URL": f"ws://localhost:{webchat_port}",
        "MCP_WEBCHAT_ACCESS_KEY": access_key,
    }
}

# Webchat channel
config.setdefault("channels", {})
config["channels"]["webchat"] = {
    "enabled": True,
    "host": os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", "0.0.0.0"),
    "port": int(webchat_port),
    "accessKey": access_key,
    "allowFrom": ["*"],
}

with open(resolved_path, "w") as f:
    json.dump(config, f, indent=2)

os.execvp("nanobot", ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace])
