##Include the following at the top before writing any code

import streamlit as st
import random

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.character_name = None
        st.session_state.land = None
        st.session_state.inventory = []
        st.session_state.phase = "character"  # character → land → explore
        st.chat_message("Jungle Master").write(
            "Hello!! I am the Jungle Master and I will be joining you on your journey in this vast wilderness!"
        )
        st.chat_message("Jungle Master").write("Now before we get started...")
        st.chat_message("Jungle Master").write("Who are you, adventurer?")

def main():
    st.title("🌴 Welcome to the Jungle! 🌴")

    initialize_session_state()

    # --- Display chat history ---
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # --- Input prompt depends on state ---
    if st.session_state.phase == "character":
        input_prompt = "Mune, Wiz, or Bruhne?"
    elif st.session_state.phase == "land":
        input_prompt = "Where do you want to go?"
    else:
        input_prompt = "Your next move?"

    # --- Chat input ---
    prompt = st.chat_input(input_prompt)
    if not prompt:
        return

    # Show player message
    with st.chat_message("adventurer"):
        st.write(prompt)
    st.session_state.messages.append({"role": "adventurer", "content": prompt})

    # --- Phase 1: Character Selection ---
    if st.session_state.phase == "character":
        characters = ["Mune", "Wiz", "Bruhne"]
        chosen_char = next((c for c in characters if c.lower() in prompt.lower()), None)

        if chosen_char:
            st.session_state.character_name = chosen_char
            st.session_state.phase = "land"

            if chosen_char == "Mune":
                response = "A charmer, I see..."
            elif chosen_char == "Wiz":
                response = "You're a wizard, Harry!"
                st.session_state.inventory.append("Map")
            elif chosen_char == "Bruhne":
                response = "A warrior, I like that!"

            begin1 = f"Welcome welcome, {chosen_char}! Your journey awaits!"
            begin2 = (
                "You are given a map, 300, 000 gold coins and a compass."
                " The map shows three landmarks: jungle (west), market (east), "
                " and The Eagle's Nest (north). Where do you want to go?"
            )

            for msg in [response, begin1, begin2]:
                with st.chat_message("Jungle Master"):
                    st.write(msg)
                st.session_state.messages.append({"role": "Jungle Master", "content": msg})

            st.rerun()

        else:
            msg = "I don’t recognize that name. Aren't you one of the menacing triplets? Mune, Wiz and Bruhne?"
            with st.chat_message("Jungle Master"):
                st.write(msg)
            st.session_state.messages.append({"role": "Jungle Master", "content": msg})

    # --- Phase 2: Land Selection ---
    elif st.session_state.phase == "land":
        choice = prompt.lower()

        available_lands = ["jungle", "market", "eagle's nest"]
        if "Map" in st.session_state.inventory:
            available_lands.append("village")

        if "jungle" in choice:
            st.session_state.land = "jungle"
            st.session_state.phase = "explore"
            msg1 = "Ah, the jungle! A place of mystery and danger..."
            msg2 = "You see a huge rock and a log blocking the river. Do you check the 'rock' or the 'log'?"
            for msg in [msg1, msg2]:
                with st.chat_message("Jungle Master"):
                    st.write(msg)
                st.session_state.messages.append({"role": "Jungle Master", "content": msg})
            st.rerun()

        elif "market" in choice:
            st.session_state.land = "market"
            st.session_state.phase = "explore"
            msg1 = "Ahh... The market. A place where you can find all sorts of treasures. And lunch. Just make sure you don't stumble upon a rowdy boy and his pet monkey. They're quite troublesome."
            msg2 = "A wandering trader approaches you and promotes his inventory. A machete, an extention to a simple map, a single gem, and a golden crown."
            for msg in [msg1, msg2]:
                with st.chat_message("Jungle Master"):
                    st.write(msg)
                st.session_state.messages.append({"role": "Jungle Master", "content": msg})
            st.rerun()

        elif "eagle" in choice:
            st.session_state.land = "eagle's nest"
            st.session_state.phase = "explore"
            msg1 = "The Eagle's Nest. I fear this place. I promised her. But if that's your choice, I'll have no choice but to comply."
            msg2 = "It's just a cave. Some say, there's a huge Eagle whom have lived thousands of years that resides here. And anyone who dares step foot in it's chambers, a painful illness will surely chase them to death."
            msg3 = "An indent the shape of a hexagon is stationed right outside of the cave entrance."
            for msg in [msg1, msg2]:
                with st.chat_message("Jungle Master"):
                    st.write(msg)
                st.session_state.messages.append({"role": "Jungle Master", "content": msg})
            st.rerun()
        
        elif "village" in choice and "Map" in st.session_state.inventory:
            st.session_state.land = "village"
            st.session_state.phase = "explore"
            msg1 = "The map allows you to see another landmark, the abandoned village."

        else:
            msg = "That place isn’t on the map. Choose jungle, market, or eagle's nest!"
            with st.chat_message("Jungle Master"):
                st.write(msg)
            st.session_state.messages.append({"role": "Jungle Master", "content": msg})

    # --- Phase 3: Exploration inside land ---
    elif st.session_state.phase == "explore":
        roll = random.randint(1, 20)
        land = st.session_state.land
        char = st.session_state.character_name

        if "leave" in prompt.lower() or "exit" in prompt.lower():
            st.session_state.phase = "land"
            st.session_state.land = "none"
            msg = "Leaving, are we? Let's check your map and venture to other places!"
            with st.chat_message("Jungle master"):
                st.write(msg)
                st.session_state.messages.append({"role": "Jungle Master", "content": msg})
                st.rerun()

        if land == "jungle":
            if "rock" in prompt.lower():
                if char == "Bruhne" or roll > 12:
                    msg = "You turn over the rock and find a waypoint to an abandoned village!"
                else:
                    msg = "You slip on the mud while turning the rock and twist your ankle!"
            elif "log" in prompt.lower():
                if char == "Bruhne":
                    msg = "With your brute strength, you move the log and reveal a hidden waterfall!"
                else:
                    msg = "You try to move the log, but it's too heavy. Maybe you need your other triplet for this."
            else:
                msg = "Everything else is poisonous! Choose rock or log!"

        elif land == "market":
            if "machete" in prompt.lower():
                msg = "Merchant : Oooo... A machete! Me own favourite. Ye have great taste for things aintcha."
                st.session_state.inventory.append("Machete")
            elif "map" in prompt.lower():
                msg = "Merchant : Adventurer, are ye! This'll show ye all the nooks and cranny of this world. "
                st.session_state.inventory.append("Map")
            elif "gem" in prompt.lower():
                msg = "Merchant : A six sided gem, just like me own pet."
                st.session_state.inventory.append("Gem")
            elif "crown" in prompt.lower():
                if char == "Mune" :
                    msg = "Merchant : Ahh.. No wonder I felt like I've seen yer likeness before! A crown truly fit for a royalty. The price shall be free!"
                    st.session_state.inventory.append("Golden Crown")
                else :
                    msg = "Merchant : Who are ye again? Puh-lease. Likes of ye ain't worthy enough to be in tis vicinity!"
            else :
                msg = "Merchant : Ye might wanna check them others stash. Not in my shop those disgusting things. Orrr... Ye oughta change yer mind."

        elif land == "eagle's nest":
            msg = "Can't really anything. We musn't enter without something to fill the indentation."

        with st.chat_message("Jungle Master"):
            st.write(msg)
        st.session_state.messages.append({"role": "Jungle Master", "content": msg})


if __name__ == "__main__":
    main()
