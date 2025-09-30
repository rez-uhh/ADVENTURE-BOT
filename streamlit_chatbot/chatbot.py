##Include the following at the top before writing any code

import streamlit as st
import random
import streamlit as st
import random

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.character_name = None
        st.session_state.land = None
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
        input_prompt = "Where do you want to go? (jungle, market, eagle's nest)"
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
            elif chosen_char == "Bruhne":
                response = "A warrior, I like that!"

            begin1 = f"Welcome welcome, {chosen_char}! Your journey awaits!"
            begin2 = (
                "You are given a map and a compass. "
                "The map shows three landmarks: 🌲 jungle (west), 🏪 market (east), "
                "and 🦅 The Eagle's Nest (north). Where do you want to go?"
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
            msg = "The market is bustling with shady merchants. Do you 'approach' the merchant or 'ignore' him?"
            with st.chat_message("Jungle Master"):
                st.write(msg)
            st.session_state.messages.append({"role": "Jungle Master", "content": msg})
            st.rerun()

        elif "eagle" in choice:
            st.session_state.land = "eagle's nest"
            st.session_state.phase = "explore"
            msg = "The climb to the Eagle’s Nest begins. The wind howls... Will you 'hide' or 'stand tall'?"
            with st.chat_message("Jungle Master"):
                st.write(msg)
            st.session_state.messages.append({"role": "Jungle Master", "content": msg})
            st.rerun()

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
                msg = "You’re in the jungle. Try 'rock' or 'log'."

        elif land == "market":
            if "approach" in prompt.lower():
                msg = "The merchant grins slyly and offers you a glowing amulet... for a price."
            elif "ignore" in prompt.lower():
                msg = "You walk past the merchant, but you feel his eyes burning into your back..."
            else:
                msg = "You’re at the market. Will you 'approach' or 'ignore' the merchant?"

        elif land == "eagle's nest":
            if "hide" in prompt.lower():
                msg = "You duck under a boulder as a giant eagle swoops overhead!"
            elif "stand" in prompt.lower():
                msg = "The eagle notices your bravery and drops a feather of power at your feet."
            else:
                msg = "The winds howl... Will you 'hide' or 'stand tall'?"

        with st.chat_message("Jungle Master"):
            st.write(msg)
        st.session_state.messages.append({"role": "Jungle Master", "content": msg})


if __name__ == "__main__":
    main()
