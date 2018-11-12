# forced-algnment
Using the Python/C library aeneas (https://github.com/readbeyond/aeneas) to facilitate the process of providing timestamps for a set of transcripts, given a set of videos

At this stage, we are testing whether Aeneas is suitable for aligning video recordings between parents and children with sufficent accuracy to reduce the work load done by manual coders. 

If this software turns out to be suitable, we will be creating scripts to facilitate the process below.

The process of installation involved:
  * Creating a virtual environment where we install Aeneas and its dependencies
  * Install aeneas and its dependencies. This file provides instructions for each OS
	(https://github.com/readbeyond/aeneas/blob/master/wiki/INSTALL.md)
	* Install sox for cleaning the recordings:
		* `sudo apt install sox libsox-fmt-*`
		


Usage of aeneas for the purpose of aligning _a single_ video recording (as of now):
* Retrieve .mov video files from server
* Retrieve corresponding transcript from database in .txt format
* Activate the virtual environment
  * `source path/to/venv/bin/activate`
* Converting the video files (.mov specifically) to .mp3 using FFmpeg, an installed dependency for aeneas
* Cleaning the videos through sox
  *	`ffmpeg -i source.mp3 -vn -ss 00:00:18 -t 00:00:20 noisesample.wav`
  * `sox source.mp3 output.mp3 noisered noise_profile_file 0.31`
*  Run Aeneas, inputting and audio file, text file, config string, and output file (supported file types can be found here: https://github.com/readbeyond/aeneas#supported-features)
    ```
        python -m aeneas.tools.execute_task \
            path/to/audio.mp3 \
            path/to/text.txt \
            "task_language=eng|is_text_type=plain|os_task_file_format=csv|task_adjust_boundary_nonspeech_min=0.010|task_adjust_boundary_nonspeech_string=REMOVE" \
            path/to/map.csv

Currently, we are still looking into improving how the process for forced-alignment, as the resulting timestamps do not consistently match actual values.

*This process will be continually updated and scripts will be updated shortly*
