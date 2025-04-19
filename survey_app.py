# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 23:08:43 2025

@author: Lenovo
"""

# Intelligent Transportation Survey App
# Created on April 19, 2025

# Dictionary to store user responses
responses = {}

# Survey is active
polling_active = True

print("=" * 60)
print("  🚦 Welcome to the Intelligent Transportation Survey App 🚦")
print("  Making Mobility Smarter — One Idea at a Time")
print("=" * 60)

while polling_active:
    print("\n📝 New Participant Survey")
    
    name = input("👤 What is your name? ").strip().title()
    print("\n📋 Hi {}, we’d love your insights on transportation.".format(name))
    print("Please answer the following questions 👇")

    # Collect responses
    challenge = input("1️⃣ What is your biggest transportation challenge in your area? ")
    commute_time = input("2️⃣ How long does your average daily commute take (in minutes)? ")
    smart_lights = input("3️⃣ Would you support using smart traffic lights to reduce congestion? (yes/no) ")
    trust_ai = input("4️⃣ Do you think AI-powered systems can make transportation safer? (yes/no) ")
    suggested_tech = input("5️⃣ What smart transportation technology would you like to see in your city? ")

    # Save responses
    responses[name] = {
        "Challenge": challenge,
        "Commute time": commute_time,
        "support_smart_lights": smart_lights,
        "trust_ai": trust_ai,
        "suggested_tech": suggested_tech
    }

    # Ask if another person will respond
    repeat = input("\n🔁 Would you like to let another person respond? (yes/no): ").strip().lower()
    if repeat == 'no':
        polling_active = False

# Survey is complete — show results
print("\n\n✅ Survey Completed. Thank you for participating!")
print("=" * 60)
print("📊 Intelligent Transportation Survey Results")
print("=" * 60)

# Display all collected responses
for name, answers in responses.items():
    print(f"\n👤 {name}'s Responses:")
    print(f"🚧 Challenge: {answers['Challenge']}")
    print(f"🕒 Commute Time: {answers['Commute time']} minutes")
    print(f"🚦 Supports Smart Lights: {answers['support_smart_lights']}")
    print(f"🤖 Trusts AI for Safety: {answers['trust_ai']}")
    print(f"💡 Suggested Smart Tech: {answers['suggested_tech']}")
    print("-" * 50)
