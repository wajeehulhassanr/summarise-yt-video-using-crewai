import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-3.5-turbo"


import certifi
print(certifi.where())
os.environ['SSL_CERT_FILE'] = certifi.where()

from crewai import Agent, Task, Crew, Process
from tasks import identify_and_understand, summarise_video
from agents import notes_maker

crew = Crew(
    agents=[notes_maker],
    tasks=[identify_and_understand, summarise_video],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

result = crew.kickoff(inputs={"video_name": "crewAI Crash Course For Beginners-How To Create Multi AI Agent For Complex Usecases"})
print(result)