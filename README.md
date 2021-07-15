# OpenCV-python-game
It's a game of guessing the active speaker made via OpenCv-python!
This game allows its user to shift the position of a circle while watching the video. The video shows two individuals, who each take turn to speak. The user's task is to change the position of the circle appearing to the active speaker. While this is occurring, at some point I plan to change the video without the user noticing while the "game" and circle continues to show.

To achieve this purpose, I wrote the following code. The code takes the input from the user, and sends all the data to a TCP server and prints the information to a logger file. There seems to be 1 issue of audio and video synchronisation. Any help on that will be greatly appreciated.
