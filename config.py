import discord

DEFAULT_PLOTSTYLE = "dark_background"
MAIN_COLOR = "#01abe1"
MAIN_BG_COLOR = "#1d1925"

WEBHOOK_URL = "https://discord.com/api/webhooks/882334551685357578/OZ5bT6xLnHvOQzQGt1-GUcrGElY4NSPLHPBk4buVfqVKHOnI_MnLxw_rQtrvMRui0yIz"

BETA_FLAT_GRAPH_ROUTE = "/DenzGraphingApi/v1/beta_flat_graph/test/plot"
FLAT_GRAPH_ROUTE = "/DenzGraphingApi/v1/flat_graph/test/plot"
DERIVATIVE_GRAPH_ROUTE = "/DenzGraphingApi/v1/derivative_graph/test/plot"
API_HOMEPAGE_ROUTE = "/api"
API_DOCS_ROUTE = "/docs"
API_ATTRIBUTES_ROUTE = "/DenzGraphingApi/v1/attr"
API_FORM_ROUTE = "/test_form"
API_RESET_ROUTE = "/reset"
API_RICKROLL_ROUTE = "/rickroll"
LATEX_ROUTE = "/DenzGraphingApi/v1/latex/test/plot"

ERROR_ID_PLOT_STYLE = "ERROR_PLOT_STYLE_TRY_BLOCK"


async def SendLogs(text: str):
    """
    function to Use DiscordWebhook to send a msg to Discord Using Webhooks
    """
    DiscordWebhook = discord.SyncWebhook.from_url(WEBHOOK_URL)
    DiscordWebhook.send(text)
