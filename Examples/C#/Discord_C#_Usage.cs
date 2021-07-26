[Command("Graph")]
[Description("something something api link")]
public async Task Graph(CommandContext ctx, string equation, params string[] attributes)
{
  string url = $"http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot?formula={Uri.EscapeDataString(equation)}";

  foreach (var attribute in attributes)
    url += $"&{attribute}";

  using (WebClient wc = new WebClient())
  {
    var json = wc.DownloadString(url);

    if (json[0] == '{')//error
    {
      var jsonData = JsonSerializer.Deserialize<JsonData>(json);
      await ctx.Channel.SendMessageAsync(new DiscordEmbedBuilder
      {
        Title = "Graph",
        Color = Color
       }.AddField("Error", jsonData.error)
        .AddField("Error Id", jsonData.error_id)
        .AddField("Fix", jsonData.fix)).ConfigureAwait(false);
    }
    else
    await ctx.Channel.SendMessageAsync(new DiscordEmbedBuilder
      {
        Title = "Graph",
        ImageUrl = url,
        Footer = BotService.GetEmbedFooter($"Rendered by: {ctx.Member.DisplayName}"),
        Color = Color
       });
    }
 }