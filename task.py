# based on the three experiments!/usr/bin/env python
# coding=utf-8

#this script is essentially a command-line command in script form

from aeneas.tools.execute_task import ExecuteTaskCLI

ExecuteTaskCLI(use_sys=False).run(arguments=[
    None,
    u"path/to/audio.mp3", #.mp3 , .txt, and .csv are just examples, since more file types are supported
    u"path/to/text.txt", 
    u"task_language=eng|is_text_type=plain|os_task_file_format=csv|task_adjust_boundary_nonspeech_min=0.010|task_adjust_boundary_nonspeech_string=REMOVE|task_adjust_boundary_algorithm=rateaggressive|task_adjust_boundary_rate_value=14.000",
    u"path/to/output.csv"
])
