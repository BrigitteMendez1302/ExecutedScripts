mysp=__import__("my-voice-analysis")                     
p="conv1" # Audio File title
c=r"H:\Brigitte\8vo ciclo\Scripts\Processes\assets" # Path to the Audio_File directory (Python 3.7)
text = mysp.myspgend(p,c)
print('text ', text)