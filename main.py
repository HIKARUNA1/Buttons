import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all(), test_guilds=[id_вашего сервера])


@bot.event
async def on_ready():
	print(f"Бот {bot.user} готов к работе!")

#Данная кнопка будет выдавать роль

class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Текст на кнопке", style=disnake.ButtonStyle.grey, custom_id="название кнопки")
    async def red(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        role = interaction.guild.get_role(id_роли)
        if role in interaction.author.roles:
            await interaction.author.remove_roles(role)
        else:
            await interaction.author.add_roles(role)
        await interaction.response.defer()
#Повторное нажатие на кнопку убирает роль

@bot.slash_command(description='Выбери себе цвет ника')
@commands.has_permissions(administrator=True)
async def color(self, ctx):
    view = ButtonView()
    role = ctx.guild.get_role(id_роли)
  embed = disnake.Embed(color=0xF0C43F)
  embed.set_author(name="Цвет ника:")
  embed.description = f"**Люой текст**. "\
                          "**Любой текст**"
  embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
  await ctx.send(embed=embed, view=view)

bot.run("TOKEN") 
