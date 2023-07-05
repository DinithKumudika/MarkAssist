from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-7b-instruct"

answer = '''
• ACID
Atomicity
• Durability
Consistency
Isolation
6'''

scheme = '''• ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that
guarantee reliable processing of database transactions.
Atomicity
Consistency
Isolation
Durability'''

prompt = f"""Think yourself as a marker who mark exam papers by comparing student answer and marking scheme answer. Below is two sentences named as Text 1 and Text 2.
Text 1 is the answer of the marking scheme and Text 2 is the answer written by the student for a question.
Compare both Text 1 and Text 2 using both cosine similarity and semantic analysis techniques together with the context. 
then provide me a similarity score as a percentage between 0 and 1.\nText 1 : {scheme}\nText 2 : {answer}"""

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
     "text-generation",
     model=model,
     tokenizer=tokenizer,
     torch_dtype=torch.bfloat16,
     trust_remote_code=True,
     device_map="auto",
)

sequences = pipeline(
     prompt,
     max_length=200,
     do_sample=True,
     top_k=10,
     num_return_sequences=1,
     eos_token_id=tokenizer.eos_token_id,
)

for seq in sequences:
     print(f"Result: {seq['generated_text']}")