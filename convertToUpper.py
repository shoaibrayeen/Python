def toUpper(file1 , file2):
  '''
  Objective: To convert the contents of file to upperCase and save it another file
  Input Parameters:
      file1 : in which contents are in lowercase.
      file2 : where we have to save contents after converting in upperCase
  Return Value: None
  Side effect: A new file – file2 with upperCase contents is produced
  '''
  #Approach : file handling

  try:
    fIn = open(file1, 'r')
    fOut = open(file2,'w')
  except IOError:
    print('Problem in opening the file');
    sys.exit()
  line = fIn.readline()
  while(line != ''):
    fOut.write(str(line).upper())
    line = fIn.readline()
  fIn.close()
  fOut.close()

def main():
  
  '''
  Objective: To convert the contents of file to upperCase and save it another file
  Input Parameter: None
  Return Value: None
  '''
  #Approach : toUpper() function
  import sys
  sys.path.append('/home/administrator/Desktop/python')
  file1 = input('Enter file name with lowerCase contents       : ')
  file2 = input('Enter file name for saving upperCase contents : ')
  toUpper(file1,file2)

if __name__=='__main__':
  main()
