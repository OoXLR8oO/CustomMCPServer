from mcp.server.fastmcp import FastMCP


server = FastMCP()

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers and return the difference."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the product."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers and return the quotient."""
    return a / b

if __name__ == "__main__":
    server.run(transport="streamable-http")