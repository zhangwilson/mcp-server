from bilibili_api import search, sync

from mcp.server.fastmcp import FastMCP


##  define server
mcp = FastMCP('BILI MCP SERVER')


# 使用装饰器封装mcp工具
@mcp.tool()
def general_search(keyword:str):
    """
    search bilibili api with the given keyword

    args:
        keyword: str, search term to look for on bilibili

    returns:
        dictionary containing the search results from bilibili
    """
    return sync(search.search_bili(keyword))


if __name__ == '__main__':
    # mcp server 使用两种链接方式
    mcp.run(transport='stdio') # 本机链接