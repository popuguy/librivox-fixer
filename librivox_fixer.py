from pydub import AudioSegment

intro_length = 18 * 1000 #millis
outro_length = 12 * 1000 #millis

def remove_intro_outro(audio, len_intro, len_outro):
	return clip(audio, len_intro, len(audio) - len_outro)
def clip(audio, begin, end):
	return audiobook[begin:end]
if __name__ == "__main__":
	if len(argv) < 2:
		print "Usage: %s filename.mp3" % argv[0]
		exit(0)
	audiobook = AudioSegment.from_mp3(argv[1])
	audiobook = remove_intro_outro(audiobook, intro_length, outro_length)
	audiobook.export("%s_fix.mp3" % argv[1].split(".")[0], format="mp3")