AFK_HELP = """

• /afk - sets you afk.
• brb - same as afk.

"""

ADMIN_HELP = """

• /admins - list of group's staff
• /adminlist - same as /admins
• /staff - same as /admins
• /pin - pin message in chat (only admins)
• /unpin - unpin message in chat (only admins)
• /ban | /unban | /sban - bans and unbans an user (only admins)
• /mute | /unmute | /tmute - mute and unmute user (only admins)
• /kick - kick user from chat (only admins)

"""

ANIME_HELP = """

• /anime - Fetches info on single anime (includes
          buttons to look up for prequels and
          sequels)
• /character - Fetches info on multiple possible
              characters related to query
• /manga - Fetches info on multiple possible
          mangas related to query
• /airing - Fetches info on airing data for anime

"""

ANIMEQUOTES_HELP = """

• /animequotes: gives random anime quotes

"""

APPROVAL_HELP = """
 
Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send
Admin commands:
• /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
• /disapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
• /approved: List all approved users.

"""

FLOOD_HELP = """

Antiflood allows you to take action on users that send more than x messages in a row. Exceeding the set flood will result in restricting that user.

 This will mute users if they send more than 10 messages in a row, bots are ignored.
• /flood: Get the current flood control setting

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

AUTOCORRECT_HELP = """

• /autocorrect - toggle on or off

"""

BLACKLIST_HELP = """

• /addblacklist [word] - word will be deleted.
• /rmblacklist [word] - word will be removed from list.
• /blacklist - list of all blacklisted words.

"""



