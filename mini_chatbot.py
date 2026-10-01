fspeaker}: {msg['content']}")
            print("-----------------------------")
            print()
            continue

    if question.lower().strip() == "/clear":
        history =[{"role":"system","content": system_msg}]
        print("your history is cleared.start a fresh conservation.")
        print()
        continue
    if question.lower().strip() == "/help":
        print("---- Available commands ----")
        print("/history - displays conversation history")
        print("/clear- clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("----------------------------")
        print()
        continue
    
    if question.lower().strip() == "exit":
        print("chaarushya: Goodbye user. plaease come back soon!")
        print(f"you asked { question_counter} questions today.Good job!")
        break
    history.append({"role": "user", "content": question})
    question_counter +=1
    try:
        response = chat(
            model="llama3.2",
            messages =history
        )
        reply = response.message.content
        history.append({"role":"assistant","content": reply})
        print(f"chaarushya:{reply}")
        print()
    except Exception as e:
        print("unknown issue.Is ollama running?")
        
        print()T32GGGGGGGGFF                                                                                      
        # history[0]["content"] = new personality
        rom ollama import chat 

system_msg="you are a friendly tutor. Answer in warm tones.Answer in one sentence."
history=[ {"role": "system","content": system_msg}]
question_counter=0

 
while True:
    question = input("You:")
    if question == "":
        print("chaarushya: please type something.")
        continue
    if question.lower().strip()=="/history":
        print("---- your Conversation so far -----")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg ["role"]== "user":
                speaker ="you"
            else:
                speaker ="chaarushya"
            print(f"{