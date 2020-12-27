#-*-coding:utf-8-*-
import os
import re
import wave
import numpy as np
import pyaudio

#音频比对子体时间小于母体
class Voice()
	def __init__(self):
		self.name=[(x,x,x,x).....]    #音频文件转码后

	def loaddata(self,filepath):
		if type(filepath)!=str:
			print('文件的路径不正确')
			return False
		 p1=re.compile('\.wav')
		 if p1.findall(filepath) is None:
		 	print('请确保文件的格式属于wav')
		 	return False
		 try:
		 	f=wave.open(filepath,'rb')
		 	parmas=f.getparams()
		 	self.nchannels,self.sampwidth,self.framerate,self.nframes=parmas[:4]
		 	str_data=f.readframes(self.nframes)
		 	self.wave_data=np.fromstring(str_data,dtype=np.short)
		 	self.wave_data=self.wave_data.T
		 	f.close()
		 	self.name=os.path.basename(filepath) #记录下文件名
		 	return True 
		 except:
		 	print(‘File error!’)

	def fft(self,frames=40):
		block=[]
		fft_block=[]
		high_point=[]
		blocks_size=self.framerate/frames  #为每一块的frame数量
		blocks_num=self.nframes/blocks_size #将音频分块的数量
		for i in range(0,len(self.wave_data[0]))-int(blocks_size),int(blocks_size):
			block.append(self.wave_data[0][i:i+int(blocks_size)])
			fft_blocks.append(np.abs(np.fft.fft(self.wave_data[0][i:i]+int(blocks_size))))
			high_point.append((np.argmax(fft_blocks[-1][:40]),
			np.argmax(fft_blocks[-1][40:80])+40,
			np.argmax(fft_blocks[-1][80:120])+80,
			np.argmax(fft_blocks[-1][120:180])+120,))
			return high_point

	def play(self,filepath):
		chunk=1024
		wf=wave.open(filepath,'rb')
		p=pyaudio.PyAudio()
		#打开声音输出流
		stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True)
		#写声音输出流进行播放
		while True:
			data=wf.readframes(chunk)
			if data=="":
				break
			stream.write(data)
			stream.close()
			p.terminate()

	def fp_compare(self,search_fp,type):
		'''type决定音频比对类型'''
		if type=="clock":
			match_fp=self.clock
		.......
		if len(search_fp)>len(match_fp):
			return 0;
		max_similar=0
		search_fp_len=len(search_fp)
		match_fp_len=len(match_fp)
		for i in range(match_fp_len-search_fp_len):
			temp=0
			for j in range(search_fp_len):
				flag=0
				for x in range(4):
					if match_fp[i+j][x]<=search_fp[j][x]<=match_fp[i+j][x]:
						flag=flag+1
						if flag==4:
							temp+=1
						if temp>max_similar:
							max_similar=temp
		return max_similar

if __name__='__main__':
	p=Voice()
	#加载具体音频路径
	p.loaddata("outFile") 	
	#比对音频能量值 大于1为比对成功 等于0为比对失败，代表音频不匹配
	print(p.fp_compare(p.fft())) is 0)
