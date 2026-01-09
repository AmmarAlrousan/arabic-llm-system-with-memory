def build_context(memory):
    ctx = ""

    if memory["long_term"]:
        ctx += "\n[ذاكرة طويلة المدى]\n"
        for k, v in memory["long_term"].items():
            ctx += f"- {k}: {v}\n"

    if memory["short_term"]:
        ctx += "\n[آخر المحادثات]\n"
        for item in memory["short_term"][-5:]:
            ctx += f"المستخدم: {item['user']}\n"
            ctx += f"النظام: {item['assistant']}\n"

    return ctx
