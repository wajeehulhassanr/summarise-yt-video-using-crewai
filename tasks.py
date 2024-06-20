from crewai import Task
from tools import yt_tool
from agents import notes_maker

identify_and_understand = Task(
  description=("Identify the video : {video_name}"
               "Understand the topics and procedures mentioned in the identified video and collect all relavant details"),
  expected_output='Detailed parapgraphs for all relavent information from the video transcript',
  agent=notes_maker,
  tools=[yt_tool]
)

summarise_video = Task(
  description=("Arrage and structure information"
               "Structure ALL the information and procedures mentioned in the transcript WITHOUT MISSING ANY IMPORTANT DETAIL"),
  expected_output='Structured markdown with using bullets, headings and sub headings etc.',
  agent=notes_maker,
  context=[identify_and_understand],
#   tools=[yt_tool],
  output_file='summary_2.md'
)