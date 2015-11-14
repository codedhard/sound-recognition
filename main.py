import sys
sys.path.append(r"c:\python26\lib")
sys.path.append(r"C:\Python26\Lib\site-packages")
pythonPath = "C:\Program Files (x86)\IronPython 2.7\Lib"
sys.path.append(pythonPath)


from operator import add
from operator import ge

from copy import deepcopy


import threading

import sys
import math
import random
import string

import time


##random.seed(0)
#import random
###from pickle import *
import pickle


import itertools
#from multiprocessing import Pool, freeze_support
##import multiprocessing


from carver.htm import HTM
from carver.htm.ui.excite_history import ExciteHistory
from carver.htm.io.objectrecognize import ObjectRecognize
from carver.htm.io.input_encoder_line import TranslateInput



from carver.utilities.HTML_cells import HTML_cells

import math2

import php2
#import py2
Filesystem=php2.Filesystem()




import py2
IsSamePrevious_obj = py2.IsSamePrevious()


#import GLOBAL
#GLOBAL.DEBUG=False


CONFIG={}

CONFIG['threading']=True
#CONFIG['threading']=False

#GLOBAL.NETWORK_TABLE={}
NETWORK=True
#NETWORK=False

TRAINING = True
#TRAINING = False




def init():
	pass


import http_server
http_server.main()
time.sleep( 1 )

#pyaudio
def ProcessSound( Prog , Prog_id=None ):
	#crash()
	global GA_NN_obj
	#global ENERGY_init

	if Prog_id != None:
		#crash()
		Prog=GA_NN_obj.Progs[ Prog_id ]

	Prog.init3()
	Prog.Prog_ORDERS=[]
	Prog.i=1


	#PyAudio_mic( Prog )
	#time.sleep( 999 )





	wf_rand=random.randint(0, len(stream_data)-1 )

	__ORDERS2=[]
	i2=0
	range2=len( stream_data[wf_rand] )
	#len_wf_text2=len(wf_text[wf_rand])*2
	len_wf_text2=len(wf_text[wf_rand])
	while i2 < range2-1:
		i2+=1
		#Prog.ORDERS=[]
		#Prog.run( [ stream_data[wf_rand][i2] ] )

		if NETWORK==True:
			#pyaudio_stream
			data=http_server.Network_Q_obj.get_data()
			if data != None:
				print data
				data2 , target = data[:-1],data[-1]
				_data2 = map(int, data2)#convert to int
				#parseWAVE_str = str( [data,data2 , target] )
				parseWAVE_str = str( [_data2 , target] )
				Filesystem.file_put_contents("data/pyaudio_stream.txt", parseWAVE_str+"\r\n", ["FILE_APPEND"] )

				#_data22 = ', '.join(data)
				#Filesystem.file_put_contents("data/pyaudio_stream2.txt", str(_data22)+"\r\n", ["FILE_APPEND"] )
				Prog.run( _data2 , target )
			else:
				print "no data"
				time.sleep( 0.5 )
			#""
		else:
			Prog.run( stream_data[wf_rand][i2] , wf_text[wf_rand] )

	#Prog.Fitness=int(fitness)
	#return fitness


#https://people.csail.mit.edu/hubert/pyaudio/
CHUNK = 1024
#CHUNK = 512
#CHUNK = 128


#CHUNK = 4096
CHUNK = 2048
"""
			__data = ""
			HOST, PORT = "localhost",90
			__req = urllib2.Request(url="http://"+str(HOST)+":"+str(PORT)+"/",
			data=str(__data) )
			__f = urllib2.urlopen(__req)
			__info=__f.read()
"""

def parseWAVE( filename ):
	wf = wave.open( filename , 'rb')

	stream_data_temp=[]
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
				channels=wf.getnchannels(),
				rate=wf.getframerate(),
				output=True)
	data = wf.readframes(CHUNK)

	while data != '':
		#stream.write(data)
		data = wf.readframes(CHUNK)
		rmsTemp = audioop.rms(data,2)
		#print audioop.max( data,2 )
		#print audioop.maxpp( data,2 )
		audioop_minmax=audioop.minmax( data,2 )
		#print audioop_minmax
		#print rmsTemp
		#print ""
		#stream_data_temp.append( rmsTemp )
		stream_data_temp.append( [rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )] )

	stream.stop_stream()
	stream.close()

	#p.terminate()
	wf.close()

	return stream_data_temp

import threading
def recWAVE( filename , max_time=30 , callback=None ):
	#file must be a Sample file

	wf = wave.open( filename , 'rb')

	stream_data_temp=[]
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
				channels=wf.getnchannels(),
				rate=wf.getframerate(),
				output=True,
				input=True)
	#data = wf.readframes(CHUNK)
	wf.close()
	data = ' '

	max_time_timer = 0
	while data != '':


		#data = wf.readframes(CHUNK)
		data = stream.read(CHUNK)
		##stream.write(data)

		rmsTemp = audioop.rms(data,2)
		#print audioop.max( data,2 )
		#print audioop.maxpp( data,2 )
		audioop_minmax=audioop.minmax( data,2 )
		#print audioop_minmax
		#print rmsTemp
		#print ""
		#stream_data_temp.append( rmsTemp )
		##stream_data_temp.append( [rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )] )

		#if callback != None:
		#	callback.run( [rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )], None )

		#if callback != None:
		#	__t = threading.Thread(target=callback.run , args=([rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )], None) )
		#	__t.start()

		#print [rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )]
		parseWAVE_str = str([rmsTemp,audioop_minmax[0],audioop_minmax[1],audioop.maxpp( data,2 ),audioop.max( data,2 )])
		Filesystem.file_put_contents("data/recording2.txt", parseWAVE_str )

		#sockets?
		#time.sleep( 0.01 )



		max_time_timer += 1
		print "audio",max_time_timer,max_time
		if max_time==max_time_timer:
			data =""

	stream.stop_stream()
	stream.close()
	return stream_data_temp


fname = "data/word_list3.txt"
if Filesystem.file_exists( fname )==True:
	wf=[]
	stream_data=[]
	wf_text=[]
	q = Filesystem.file_get_contents( fname )

	qq=q.split("\n")
	#for i in range( len(qq)-1 ):
	CACHED_WAVE=True
	for i in range( int(len(qq)/10) ):
		print qq[i]+" "+str(i)+"/"+str(len(qq))+"@"

		fname="../data/words/"+qq[i]+".txt"
		if Filesystem.file_exists( fname )==False:
			CACHED_WAVE=False

	if CACHED_WAVE==False:
		import pyaudio
		import wave
		import sys
		import audioop

		p = pyaudio.PyAudio()
		for i in range( int(len(qq)/10) ):
			print qq[i]+" "+str(i)+"/"+str(len(qq))+"@"

			file_open1="../data/words/"+qq[i]+".wav"
			#Filesystem.file_put_contents("word_list3.txt", str(word_list3[i])+"\r\n", ["FILE_APPEND"] )
			#stream_data.append( parseWAVE(file_open1) )
			parseWAVE_list = parseWAVE(file_open1)
			stream_data.append( parseWAVE_list )
			parseWAVE_str=""
			for i2 in range( len(parseWAVE_list) ):
				parseWAVE_str+= str(parseWAVE_list[i2])+"\r\n"
			Filesystem.file_put_contents("../data/words/"+qq[i]+".txt", parseWAVE_str )

			wf_text.append( qq[i] )
		p.terminate()
	else:
		#for i in range( int(len(qq)/10) ):
		for i in range( 8 ):
			print qq[i]+" "+str(i)+"/"+str(len(qq))+"@"

			parseWAVE_list = []
			#...
			fname="../data/words/"+qq[i]+".txt"
			prog_data_raw=Filesystem.file_get_contents( fname )
			prog_data=prog_data_raw.split("\n")

			if prog_data[ len(prog_data)-1 ]=="":
				#print "!"
				del prog_data[ len(prog_data)-1 ]
			for i2 in range( len(prog_data) ):
				prog_data[i2] = eval( prog_data[i2] )
				#print "@",prog_data[i2],"$"
			parseWAVE_list.extend( prog_data )

			#print type( parseWAVE_list )
			#print type( parseWAVE_list[0] )
			#print type( parseWAVE_list[0][0] )

			#print parseWAVE_list
			stream_data.append( parseWAVE_list )

			wf_text.append( qq[i] )

test=True

"""
import pyaudio
import wave
import sys
import audioop
"""

def PyAudio_mic( _callback_Prog ):
	global p
	if test:
		"""
		import pyaudio
		import wave
		import sys
		import audioop
		"""

		print "<<<P"
		p = pyaudio.PyAudio()
		print ">>>P"
		if True:
			#print qq[i]+" "+str(i)+"/"+str(len(qq))+"@"

			file_open1="../data/words/aba.wav"

			#parseWAVE_list = parseWAVE(file_open1)
			parseWAVE_list = recWAVE( file_open1 , max_time=60 , callback=_callback_Prog )
			stream_data.append( parseWAVE_list )
			parseWAVE_str=""
			for i2 in range( len(parseWAVE_list) ):
				parseWAVE_str+= str(parseWAVE_list[i2])+"\r\n"
			Filesystem.file_put_contents("data/recording.txt", parseWAVE_str )

			wf_text.append( qq[i] )
		p.terminate()










class PROG():
	def __init__(self):
		pass

	def init3(self):
		pass
	def run(self, __val , __target ):
		print "run()",__val, __target


def main():
	__Prog = PROG()
	ProcessSound( Prog=__Prog , Prog_id=None )
	__Prog.dump()
	ProcessSound( Prog=__Prog , Prog_id=None )

	for i in range( 100 ):
		ProcessSound( Prog=__Prog , Prog_id=None )
		if i%20==0:
			__Prog.dump()
	__Prog.dump()

	print "The End"

class BRAIN:
	def __init__(self):
		pass
	def run(self):
		i=0
		while i<1000:
			print "run()"
			#print "data=",Network_Q_obj.get_data()
			print "data=",http_server.Network_Q_obj.get_data()
			#time.sleep( 1 )
			time.sleep( 0.5 )

			#http_server.Network_Q_obj.set_data( [i] )

			i+=1


def main2():
	http_server.main()
	time.sleep( 1 )

	print "..."

	_BRAIN=BRAIN()

	t2 = threading.Thread( target=_BRAIN.run )
	t2.start()

if __name__ == '__main__':
	#global pool
	#pool = multiprocessing.Pool( 2 )
	#pool = multiprocessing.Pool( 8 )

	init()
	main()
	##PAUSE=raw_input('Press Enter to continue...')
