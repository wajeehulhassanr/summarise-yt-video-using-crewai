from crewai import Agent
from tools import yt_tool

notes_maker = Agent(
  role='Notes creater for Youtube Videos',
  goal="""Get transcript of video specific to following topic : {video_name} and write detailed notes wiht relavant information in structured markdown""",
  backstory="""A skilled Data Scientist who is expert in structuring important information and procedures, hired to write blogs from youtube videos""",
  tools=[yt_tool],  # Optional, defaults to an empty list
  max_rpm=10, # Optional
  verbose=True,  # Optional
  allow_delegation=True,  # Optional
  cache=True  # Optional
)
