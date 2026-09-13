import os
from mcp.server.fastmcp import FastMCP
port = int(os.environ.get("PORT",10000))

mcp = FastMCP(
          "Reversewordserver",
          host = "0.0.0.0",
          port = port,
          stateless_http = True,
          json_response=True
)
@mcp.tool(description="Reverse a single word .Example : 'habeeb' -> 'beebah'")
def reverse_word(word:str) ->str:
  """Reverse a single word."""
  return word[::-1]
if __name__ == "__main__":
  mcp.run(transport="streamable-http")
