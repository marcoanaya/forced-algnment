# based on the three experiments!/usr/bin/env python
# coding=utf-8

from aeneas.executetask import ExecuteTask
from aeneas.task import Task

config_string =(
    u"task_language=eng|" + 
    u"is_text_type=plain|" + #
    u"os_task_file_format=csv|" + # output file type
    u"task_adjust_boundary_nonspeech_min=0.010|" + # consider timestamps of nonspeech if they are longer than .10 sec
    u"task_adjust_boundary_nonspeech_string=REMOVE|" + # remove nonspeech timestamps
    u"task_adjust_boundary_algorithm=rateaggressive|" + 
    u"task_adjust_boundary_rate_value=14.000")
task = Task(config_string=config_string)
task.audio_file_path_absolute = u"audio/test-sox-low.mp3"
task.text_file_path_absolute = u"transcripts/test.txt"
task.sync_map_file_path_absolute = u"output/test-sox3.csv"

ExecuteTask(task).execute()

task.output_sync_map_file()
