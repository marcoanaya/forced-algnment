# Forced Alignment LDP Project

We are looking to facilitate the process of providing timestamps for a set of transcripts, given a set of corresponding videos. The goal is to reduce the amount of manual coding that needs to be done.



## Aeneas

Currently, we have been testing the Python/C library aeneas [(repo)](https://github.com/readbeyond/aeneas), created by Alberto Pettarin.
Useful websites to find more information, besides the repository, have been:
* [The documentation website](https://www.readbeyond.it/aeneas/docs/index.html)
* [aeneas-forced-alignment Google Group](https://groups.google.com/forum/#!forum/aeneas-forced-alignment). Alberto seems very open to help troubleshoot his software, so contacting him through the group could be helpful



### Installation
  * (Optional) Creating a virtual environment where we install Aeneas and its dependencies
  * Install aeneas and its dependencies. [This file](https://github.com/readbeyond/aeneas/blob/master/wiki/INSTALL.md) provides instructions for each OS

		

### Usage
Usage of aeneas for the purpose of aligning _a single_ video recording to its corresponding transcript:
* [*Supported file types can be found here!*](https://github.com/readbeyond/aeneas#supported-features)
* (If necessary) Preparing the input files
	* Retrieve video files from server
	* Retrieve corresponding transcripts from database in a supported input format
* (Optional) Activate the virtual environment
	* `source path/to/venv/bin/activate`
* Convert video files to a supported input audio format using FFmpeg, an installed dependency for aeneas
	* For example: `ffmpeg -i input_file.mov output_file.mp3`

*  Run Aeneas, inputting and audio file, text file, config string, and output file.  
	* Below is the most simple way of running aeneas, through the command line.
	```
        python -m aeneas.tools.execute_task \
            path/to/audio.mp3 \
            path/to/text.txt \
            "task_language=eng|is_text_type=plain|os_task_file_format=csv" \
            path/to/map.csv
* *MORE IN PROGREESS*


### Background Noise

We found that there was sufficent background noise in our video recording that aeneas could not distinguish the noise from actual speech. This caused two problems: Each time stamp would begin where the last one ended (undesirable for our purposes), and aeneas would generally have very poor accuracy. A solution was to pass the audio recordings through software that would reduce background noise.


#### SoX
SoX

* Install sSoX:
	* `sudo apt install sox libsox-fmt-*`
* (Before running aeneas) Cleaning the videos through sox
	*	`ffmpeg -i path/to/source.mp3 -vn -ss 00:00:18 -t 00:00:20 noisesample.wav`
	* `sox source.mp3 path/to/output.mp3 noisered noise_profile_file 0.31`
		
Currently, we are still looking into improving how the process for forced-alignment, as the resulting timestamps do not consistently match actual values.

