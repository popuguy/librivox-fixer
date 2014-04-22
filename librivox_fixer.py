from pydub import AudioSegment

if __name__ == "__main__":
	if len(argv) < 2:
		print "Usage: %s filename.mp3" % argv[0]
		exit(0)
	audiobook = AudioSegment.from_mp3(argv[1])
	intro_length = 18 * 1000 #ms
	outro_length = 12 * 1000 #ms
	audiobook = audiobook[intro_length:len(audiobook) - outro_length]
	audiobook.export("%s_fix.mp3" % argv[1].split(".")[0], format="mp3")