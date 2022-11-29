from pyrogram import Client, filters, enums
import time

RELOAD = False

admin_list = {}

async def list_admins(_: Client, chat_id: int):
    global admin_list
    if not chat_id in admin_list:
        l = await reload_admins(_, chat_id)
        admin_list[chat_id] = {"admins": l, "updated": time.time()}
        return l
    if (int(time.time()-admin_list[chat_id]["updated"])) >= 600:
        l = await reload_admins(_, chat_id)
        admin_list[chat_id] = {"admins": l, "updated": time.time()}
        return l
    if RELOAD:
        l = await reload_admins(_, chat_id)
        admin_list[chat_id] = {"admins": l, "updated": time.time()}
        return l
    return admin_list[chat_id]["admins"]

async def reload_admins(_: Client, chat_id: int):
    l = []
    async for x in _.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        l.append(x.user.id)
    return l

admin_rights = {}

async def list_admin_rights(_: Client, chat_id: int):
    global admin_rights
    l = await list_admins(_, chat_id)
    if not chat_id in admin_rights:
        for x in l:
            h = await _.get_chat_member(chat_id, x)
            h = h.privileges
            admin_rights = {chat_id: {x: {"can_change_info": True if h.can_change_info else False}}}
            admin_rights = {chat_id: {x: {"can_delete_messages": True if h.can_delete_messages else False}}}
            admin_rights = {chat_id: {x: {"can_restrict_members": True if h.can_restrict_members else False}}}
            admin_rights = {chat_id: {x: {"can_promote_members": True if h.can_promote_members else False}}}
            admin_rights = {chat_id: {x: {"can_invite_users": True if h.can_invite_users else False}}}
            admin_rights = {chat_id: {x: {"can_pin_messages": True if h.can_pin_messages else False}}}
            admin_rights = {chat_id: {x: {"can_manage_video_chats": True if h.can_manage_video_chats else False}}}
        admin_rights[chat_id]["updated"] = time.time()
        return admin_rights
    if (int(time.time() - admin_rights[chat_id]["updated"])) > 3600:
        for x in l:
            h = await _.get_chat_member(chat_id, x)
            h = h.privileges
            admin_rights = {chat_id: {x: {"can_change_info": True if h.can_change_info else False}}}
            admin_rights = {chat_id: {x: {"can_delete_messages": True if h.can_delete_messages else False}}}
            admin_rights = {chat_id: {x: {"can_restrict_members": True if h.can_restrict_members else False}}}
            admin_rights = {chat_id: {x: {"can_promote_members": True if h.can_promote_members else False}}}
            admin_rights = {chat_id: {x: {"can_invite_users": True if h.can_invite_users else False}}}
            admin_rights = {chat_id: {x: {"can_pin_messages": True if h.can_pin_messages else False}}}
            admin_rights = {chat_id: {x: {"can_manage_video_chats": True if h.can_manage_video_chats else False}}}
        admin_rights[chat_id]["updated"] = time.time()
        return admin_rights
    if RELOAD:
        for x in l:
            h = await _.get_chat_member(chat_id, x)
            h = h.privileges
            admin_rights = {chat_id: {x: {"can_change_info": True if h.can_change_info else False}}}
            admin_rights = {chat_id: {x: {"can_delete_messages": True if h.can_delete_messages else False}}}
            admin_rights = {chat_id: {x: {"can_restrict_members": True if h.can_restrict_members else False}}}
            admin_rights = {chat_id: {x: {"can_promote_members": True if h.can_promote_members else False}}}
            admin_rights = {chat_id: {x: {"can_invite_users": True if h.can_invite_users else False}}}
            admin_rights = {chat_id: {x: {"can_pin_messages": True if h.can_pin_messages else False}}}
            admin_rights = {chat_id: {x: {"can_manage_video_chats": True if h.can_manage_video_chats else False}}}
        admin_rights[chat_id]["updated"] = time.time()
        return admin_rights
    return admin_rights 

@Client.on_message(filters.command("reload") & filters.group)
async def reload(_, m):
    global RELOAD
    RELOAD = True
    ok = await m.reply(f"**Reloading bot...\n\n• loading\n\n• ⏳\n\n• ⏳\n\n• ⏳**")
    x = await list_admins(_, m.chat.id)
    await ok.edit(f"**Reloading bot...\n\n• loading\n\n• Admin list updated ✅\n\n• ⏳\n\n• ⏳**")
    x = await list_admin_rights(_, m.chat.id)
    text = f"reloaded admin rights ✅"
    await ok.edit(f"**Reloading bot...\n\n• loading\n\n• Admin list updated ✅\n\n• {text}\n\n• ⏳**")
    RELOAD = False
    x = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, x)
    x = x.privileges
    if not x.can_restrict_members:
        txt = "No ban rights ❌"
    else:
        txt = "Bot can ban ✅"
    await ok.edit(f"**Reloaded bot !\n\n• loaded\n\n• Admin list updated ✅\n\n• {text}\n\n• {txt}**")
    
