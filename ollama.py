import ollama

def get_completion(model, messages):
  data = {
  "model": model,
  "messages": messages,
  "stream": False
  }
  return ollama.chat(**data)['message']['content']


docs = "" # 사내 문서
summary_messages = [
	  { "role": "system", "content": "너는 요약하는 어시스턴트야. 한국어로 한줄로 요약해줘" },
    { "role": "user", "content": docs }]
get_completion('llama3', summary_messages)

messages = [{ "role": "user", "content":"1부터 m까지의 자연수를 작은수부터 큰 순으로 정렬해줘 #예시 질문: 1,3 답변: 1,2,3 #실제 질문: 1,10" }]
get_completion('llama3', messages)

messages = [{ "role": "user", "content":"sorted(range(1,m))과 동일한 동작을 해줘 #예시 질문: 5 답변: [1,2,3,4,5] #실제 질문: 10" }]
get_completion('llama3', messages)
