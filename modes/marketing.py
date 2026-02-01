def marketing_agent(user_input):
    text = user_input.lower().strip()

    # SHOW MARKETING MENU
    if text in ["marketing", "menu", "start"]:
        return (
            "📈 *Digital Marketing Course*\n\n"
            "Choose a topic:\n"
            "1️⃣ SEO (Search Engine Optimization)\n"
            "2️⃣ Google Ads (PPC)\n"
            "3️⃣ Social Media Marketing\n"
            "4️⃣ Email Marketing\n"
            "5️⃣ Content Marketing\n"
            "6️⃣ Analytics & Tools\n\n"
            "Reply with *1–6*"
        )

    # SEO
    if text == "1":
        return (
            "🔍 *SEO Course*\n\n"
            "• Keyword Research\n"
            "• On-Page SEO\n"
            "• Technical SEO\n"
            "• Backlinks\n"
            "• Google Search Console\n"
            "• SEO Tools (Ahrefs, SEMrush)"
        )

    # GOOGLE ADS
    if text == "2":
        return (
            "💰 *Google Ads*\n\n"
            "• Account Setup\n"
            "• Keyword Planner\n"
            "• Search Ads\n"
            "• Display Ads\n"
            "• YouTube Ads\n"
            "• Conversion Tracking"
        )

    # SOCIAL MEDIA
    if text == "3":
        return (
            "📱 *Social Media Marketing*\n\n"
            "• Facebook & Instagram Ads\n"
            "• LinkedIn Marketing\n"
            "• YouTube Growth\n"
            "• Content Strategy\n"
            "• Influencer Marketing"
        )

    # EMAIL
    if text == "4":
        return (
            "📧 *Email Marketing*\n\n"
            "• Lead Funnels\n"
            "• Mailchimp\n"
            "• Automation\n"
            "• Campaign Strategy\n"
            "• Open & CTR Optimization"
        )

    # CONTENT
    if text == "5":
        return (
            "✍️ *Content Marketing*\n\n"
            "• Blogging\n"
            "• Copywriting\n"
            "• Landing Pages\n"
            "• Video Marketing\n"
            "• AI Content Tools"
        )

    # ANALYTICS
    if text == "6":
        return (
            "📊 *Analytics & Tools*\n\n"
            "• Google Analytics 4\n"
            "• Google Tag Manager\n"
            "• Search Console\n"
            "• Heatmaps\n"
            "• Conversion Tracking"
        )

    return "⚠️ Please choose a valid marketing option (1–6)."
