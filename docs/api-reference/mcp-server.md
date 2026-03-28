---
search:
  exclude: true
---

# MCP Server API Reference

The **CybrScrape MCP Server** provides six powerful tools for web scraping through the Model Context Protocol (MCP). This server integrates CybrScrape's capabilities directly into AI chatbots and agents, allowing conversational web scraping with advanced anti-bot bypass features.

You can start the MCP server by running:

```bash
cybrscrape mcp
```

Or import the server class directly:

```python
from cybrscrape.core.ai import CybrScrapeMCPServer

server = CybrScrapeMCPServer()
server.serve(http=False, host="0.0.0.0", port=8000)
```

## Response Model

The standardized response structure that's returned by all MCP server tools:

## ::: cybrscrape.core.ai.ResponseModel
    handler: python
    :docstring:

## MCP Server Class

The main MCP server class that provides all web scraping tools:

## ::: cybrscrape.core.ai.CybrScrapeMCPServer
    handler: python
    :docstring: