AFK_HELP = """

Here is the help for the AFK💤 module:

 • /afk <reason>: mark yourself as AFK(away from keyboard).
 • brb <reason>: same as the afk command - but not a command.
When marked as AFK, any mentions will be replied to with a message to say you're not available!

"""

ADMIN_HELP = """

Here is the help for the Admins module:

• /admins: list of admins in the chat
Admins only:
 • /pin: silently pins the message replied to - add 'loud' or 'notify' to give notifs to users
 • /unpin: unpins the currently pinned message
 • /invitelink: gets invitelink
 • /promote: promotes the user replied to
 • /fullpromote: Fully promotes the user replied to
 • /demote: demotes the user replied to
 • /title <title here>: sets a custom title for an admin that the bot promoted
 • /admincache: force refresh the admins list
 • /setgtitle <text>: set group title
 • /setgpic: reply to an image to set as group photo
 • /setdesc: Set group description

"""

ANIME_HELP = """

Here is the help for the Anime ♓ module:

 ◆/anime - Fetches info on single anime (includes
          buttons to look up for prequels and
          sequels)
 ◆/character - Fetches info on multiple possible
              characters related to query
 ◆/manga - Fetches info on multiple possible
          mangas related to query
 ◆/airing - Fetches info on airing data for anime

"""

ANIMEQUOTES_HELP = """

Here is the help for the AnimeQuotes🖍 module:


 • /animequotes: gives random anime quotes

"""

ANTICHANNEL_HELP = """

Here is the help for the Antichannel❌ module:

Admin command :-

❖ /antichannel (on/yes/off/no) - after enabling this it will ban and delete channel user mesaages. 
 
 If u want to ban only a specific channel then reply that channel with /ban  and to unban it reply /unban

"""

APPROVAL_HELP = """

Here is the help for the Approval✅ module:
 
Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send
Admin commands:
❂ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
❂ /disapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
❂ /approved: List all approved users.

"""

FLOOD_HELP = """

Here is the help for the Anti-Flood🛡 module:

Antiflood allows you to take action on users that send more than x messages in a row. Exceeding the set flood will result in restricting that user.

 This will mute users if they send more than 10 messages in a row, bots are ignored.
 • /flood: Get the current flood control setting

• Admins only:
 • /setflood <int/'no'/'off'>: enables or disables flood control
 Example: /setflood 10
 • /setfloodmode <ban/kick/mute/tban/tmute> <value>: Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban

• Note:
 • Value must be filled for tban and tmute!!
 It can be:
 5m = 5 minutes
 6h = 6 hours
 3d = 3 days
 1w = 1 week

"""

BAN_HELP = """

Here is the help for the Bans/Mutes module:

User Commands:
  ➢ /kickme: kicks the user who issued the command
  
Admins only:
  ➢ /ban <userhandle>: bans a user. (via handle, or reply)
  banme
  ➢ /sban <userhandle>: Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)

  ➢ /unban <userhandle>: unbans a user. (via handle, or reply)

  ➢ /kick <userhandle>: kicks a user out of the group, (via handle, or reply)

"""

BLACKLIST_HELP = """

Here is the help for the Blacklists⚠️ module:


Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!

NOTE: Blacklists do not affect group admins.

 • /blacklist: View the current blacklisted words.

Admin only:
 • /addblacklist <triggers>: Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
 • /rmblacklist <triggers>: Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
 • /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>: Action to perform when someone sends blacklisted words.

"""

CHATBOT_HELP = """

Here is the help for the Chatbot💬 module:

Admin command (only admins can use in group)

Note :- u can use it in bot pm freely and you can chat only by replying bot messages.

❖ /chatbot  - Togle buttons for Control panel ( enable and disable )

  Bot AI supports many languages we hope u all would have fun.

"""

EXTRA_HELP = """

Here is the help for the Extras🎐 module:

Available commands:
Markdown:
 • /markdownhelp: quick summary of how markdown works in telegram - can only be called in private chats

Paste:
 • /paste : Saves replied content to paster and replies with a url and content pic.

React:
 • /react : Reacts with a random reaction 

Urban Dictonary:
 • /ud <word>: Type the word or expression you want to search use

Wikipedia:
 • /wiki <query>: wikipedia your query

Wallpapers:
 • /wall <query>: get a wallpaper from wall.alphacoders.com

Currency converter: 
 • /cash : currency converter
Example:
 /cash 1 USD INR 
      OR
 /cash 1 usd inr
Output: 1.0 USD = 75.505 INR

Shippering: 
 • /couples : chooses random 2 people in the chat and ships them
             Note: New couples can be again choosen after 24 hrs with same command.

"""

FILTERS_HELP = """

Here is the help for the Filters🔖 module:

  ➢ /filters: List all active filters saved in the chat.
Admin only:
  ➢ /filter <keyword> <reply message>: Add a filter to this chat. The bot will now reply that message whenever 'keyword'is mentioned. If you reply to a sticker with a keyword, the bot will reply with that sticker. NOTE: all filter keywords are in lowercase. If you want your keyword to be a sentence, use quotes. eg: /filter "hey there" How you doin?
 Separate diff replies by %%% to get random replies
 Example: 
 /filter "filtername"
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3
  ➢ /stop <filter keyword>: Stop that filter.
Chat creator only:
  ➢ /removeallfilters: Remove all chat filters at once.

"""

FUN_HELP = """

Here is the help for the Fun module:

 • /runs - reply a random string from an array of replies
 • /slap - slap a user, or get slapped if not a reply
 • /shrug - get shrug XD
 • /table - get flip/unflip :v
 • /decide - Randomly answers yes/no/maybe
 • /toss - Tosses A coin
 • /bluetext - check urself :V
 • /meme - random anime memes
 • /roll - Roll a dice
 • /rlg - Join ears,nose,mouth and create an emo ;-;
 • /shout <keyword> - write anything you want to give loud shout
 • /weebify <text> - returns a weebified text
 • /sanitize - always use this before /pat or any contact
 • /pat - pats a user, or get patted

"""

GIT_HELP = """

Here is the help for the Github😸 module:

 /gitinfo :- <github profile username>
Get info of any github profile.

"""

GOOGLE_HELP = """

Here is the help for the Google🔎 module:

 • /google <text> :- Perform a google search
 • /img <text> :- Search Google for images and returns them
For greater no. of results specify lim, For eg: /img hello lim=10
 • /app <appname> :- Searches for an app in Play Store and returns its details.
 • /grs <reply to image> :- Same like /reverse.

"""





